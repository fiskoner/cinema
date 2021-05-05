from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=255, default='', blank=True, verbose_name='Название фильма')
    description = models.TextField(blank=True, default='', verbose_name='Описание фильма')
    release_date = models.DateField(null=True)
    duration = models.DurationField(null=True)
    countries = models.ManyToManyField('directory.Country', related_name='movies')
    genres = models.ManyToManyField('directory.MovieGenre', related_name='movies')

    class Meta:
        verbose_name = 'Кино'
        verbose_name_plural = 'Кино'

    def __str__(self):
        return self.name


class MoviePhoto(models.Model):

    def get_images_upload_path(self, filename):
        return f'movies/{self.movie.name}/{filename}'

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='photos')
    image = models.FileField(upload_to=get_images_upload_path)
    is_title = models.BooleanField(null=True, unique=True)  # SHIT CODE BUT ITS WORKING

    def __str__(self):
        return self.movie.name