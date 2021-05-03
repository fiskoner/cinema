from django.db import models

# Create your models here.


def get_images_upload_path(self, instance, filename):
    return f'movies/{instance.release_date}/{instance.name}/{filename}'


class Movie(models.Model):
    name = models.CharField(max_length=255, default='', blank=True, verbose_name='Название фильма')
    release_date = models.DateField(null=True)
    duration = models.DurationField(null=True)

    class Meta:
        verbose_name = 'Кино'
        verbose_name_plural = 'Кино'


class MoviePhoto(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='photos')
    image = models.FileField(upload_to=get_images_upload_path)
