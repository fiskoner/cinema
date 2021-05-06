from django.contrib import admin

# Register your models here.
from directory.mixins.admin_mixins import ImageInlineMixin
from movies import models
from directory import models as directory_models


class MoviePhotoInline(ImageInlineMixin):
    model = models.MoviePhoto


class ActorInline(admin.TabularInline):
    model = directory_models.Actor.movies.through


class MovieDirectorInline(admin.TabularInline):
    model = directory_models.MovieDirector.movies.through


class MovieGenreInline(admin.TabularInline):
    model = models.Movie.genres.through


class CountryInline(admin.TabularInline):
    model = models.Movie.countries.through


class MovieAdmin(admin.ModelAdmin):
    inlines = (MoviePhotoInline, ActorInline, MovieDirectorInline, MovieGenreInline, CountryInline)
    list_display = ('id', 'name', 'release_date', 'duration')
    exclude = ('countries', 'genres')


admin.site.register(models.Movie, MovieAdmin)
