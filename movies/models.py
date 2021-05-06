from django.db import models

# Create your models here.
from core.models import User


class Movie(models.Model):
    name = models.CharField(max_length=255, default='', blank=True, verbose_name='Название фильма')
    description = models.TextField(blank=True, default='', verbose_name='Описание фильма')
    release_date = models.DateField(null=True)
    duration = models.DurationField(null=True)
    countries = models.ManyToManyField('directory.Country', related_name='movies')
    genres = models.ManyToManyField('directory.MovieGenre', related_name='movies')
    rating = models.FloatField(default=0)
    user_rated = models.ManyToManyField(User, related_name='movies', through='movies.UserMovieRating')

    class Meta:
        verbose_name = 'Кино'
        verbose_name_plural = 'Кино'

    def __str__(self):
        return self.name


class UserMovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField(default=0)

    def count_movie_rating(self):
        movie = self.movie
        movie_ratings = UserMovieRating.objects.filter(movie=movie).exclude(pk=self.pk)
        ratings_count = movie_ratings.count()
        ratings = list(movie_ratings.values_list('rating', flat=True))
        movie_rating = (sum(ratings) + self.rating) / (ratings_count + 1)
        self.movie.rating = round(movie_rating, 2)
        self.movie.save(update_fields=['rating'])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.count_movie_rating()
        return super(UserMovieRating, self).save(force_insert, force_update, using, update_fields)


class MoviePhoto(models.Model):

    def get_images_upload_path(self, filename):
        return f'movies/{self.movie.name}/{filename}'

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='photos')
    image = models.FileField(upload_to=get_images_upload_path)
    is_title = models.BooleanField(null=True, unique=True)  # SHIT CODE BUT ITS WORKING

    def __str__(self):
        return self.movie.name
