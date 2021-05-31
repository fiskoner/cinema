from django.db import models

# Create your models here.
from rest_framework import exceptions

from directory.mixins import models_mixins
from movies.models import Movie


class Actor(models_mixins.PersonDescription):
    movies = models.ManyToManyField(Movie, through='directory.ActorMovie', related_name='actor')
    country = models.ForeignKey(
        'directory.Country', null=True, blank=True, on_delete=models.SET_NULL, related_name='actors'
    )

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'

    def __str__(self):
        return self.name


class ActorPhoto(models.Model):

    def get_images_upload_path(self, filename):
        return f'actors/{self.actor.name}/{filename}'

    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='photos')
    image = models.FileField(upload_to=get_images_upload_path)
    is_title = models.BooleanField(null=True)  # SHIT CODE BUT ITS WORKING

    def __str__(self):
        return self.actor.name

    class Meta:
        unique_together = ('actor', 'is_title',)


class ActorMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='actors')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, default='', blank=True)

    class Meta:
        verbose_name = 'Актёр в кино'
        verbose_name_plural = 'Актёры в кино'
        unique_together = ('movie', 'actor')

    def __str__(self):
        return f'{self.movie}, {self.actor} - роль "{self.role}"'


class MovieDirector(models_mixins.PersonDescription):
    movies = models.ManyToManyField(Movie, related_name='directors', blank=True)
    country = models.ForeignKey(
        'directory.Country', null=True, blank=True, on_delete=models.SET_NULL, related_name='movie_directors'
    )

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

    def __str__(self):
        return f'{self.name}'


class MovieDirectorPhoto(models.Model):

    def get_images_upload_path(self, filename):
        return f'movies_directors/{self.movie_director.name}/{filename}'

    movie_director = models.ForeignKey(MovieDirector, on_delete=models.CASCADE, related_name='photos')
    image = models.FileField(upload_to=get_images_upload_path)
    is_title = models.BooleanField(null=True)  # SHIT CODE BUT ITS WORKING

    def __str__(self):
        return self.movie_director.name

    class Meta:
        unique_together = ('movie_director', 'is_title',)


class MovieGenre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Жанр кино'
        verbose_name_plural = 'Жанры кино'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
