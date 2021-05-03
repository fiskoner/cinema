from django.db import models

# Create your models here.


def get_images_upload_path(instance, filename):
    return f'movies/{instance.movie.release_date}/{instance.movie.name}/{filename}'


class Movie(models.Model):
    name = models.CharField(max_length=255, default='', blank=True, verbose_name='Название фильма')
    description = models.TextField(blank=True, default='', verbose_name='Описание фильма')
    release_date = models.DateField(null=True)
    duration = models.DurationField(null=True)

    class Meta:
        verbose_name = 'Кино'
        verbose_name_plural = 'Кино'


class MoviePhoto(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='photos')
    image = models.FileField(upload_to=get_images_upload_path)
