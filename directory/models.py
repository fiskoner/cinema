from django.db import models
from directory import mixins

# Create your models here.
from movies.models import Movie


class Actor(mixins.PersonDescription):
    movies = models.ManyToManyField(Movie, through='directory.ActorMovie', related_name='actor')


class ActorMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='actors')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, default='', blank=True)


class MovieDirector(mixins.PersonDescription):
    movies = models.ManyToManyField(Movie, related_name='directors')


class MovieGenre(models.Model):
    name = models.CharField(max_length=100)

