from django.db import models

# Create your models here.
from directory.mixins import models_mixins
from movies.models import Movie


class Actor(models_mixins.PersonDescription):
    movies = models.ManyToManyField(Movie, through='directory.ActorMovie', related_name='actor')


class ActorMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='actors')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, default='', blank=True)


class MovieDirector(models_mixins.PersonDescription):
    movies = models.ManyToManyField(Movie, related_name='directors')


class MovieGenre(models.Model):
    name = models.CharField(max_length=100)

