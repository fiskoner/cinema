from django.db import models

# Create your models here.
from directory.mixins import models_mixins
from movies.models import Movie


class Actor(models_mixins.PersonDescription):
    movies = models.ManyToManyField(Movie, through='directory.ActorMovie', related_name='actor')
    country = models.ForeignKey('directory.Country', on_delete=models.SET_NULL, null=True, related_name='actors')

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'


class ActorPhoto(models.Model):

    def get_images_upload_path(self, filename):
        return f'actors/{self.actor.name}/{filename}'

    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='photos')
    image = models.FileField(upload_to=get_images_upload_path)


class ActorMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='actors')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, default='', blank=True)

    class Meta:
        verbose_name = 'Актёр в кино'
        verbose_name_plural = 'Актёры в кино'


class MovieDirector(models_mixins.PersonDescription):
    movies = models.ManyToManyField(Movie, related_name='directors')
    country = models.ForeignKey(
        'directory.Country', on_delete=models.SET_NULL, null=True, related_name='movie_directors'
    )

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class MovieDirectorPhoto(models.Model):

    def get_images_upload_path(self, filename):
        return f'movies_directors/{self.movie_director.name}/{filename}'

    movie_director = models.ForeignKey(MovieDirector, on_delete=models.CASCADE, related_name='photos')
    image = models.FileField(upload_to=get_images_upload_path)


class MovieGenre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Жанр кино'
        verbose_name_plural = 'Жанры кино'


class Country(models.Model):
    name = models.CharField(max_length=100)
