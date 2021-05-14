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


class MovieVideoFilesAdmin(admin.StackedInline):
    model = models.MovieVideoFiles
    verbose_name = 'Подписка'
    verbose_name_plural = 'Подписки'


class MovieSubscriptionInline(admin.TabularInline):
    model = models.Movie.subscriptions.through
    verbose_name = 'Подписка'
    verbose_name_plural = 'Подписки'


class MovieAdmin(admin.ModelAdmin):
    inlines = (MoviePhotoInline, ActorInline, MovieDirectorInline, MovieGenreInline, CountryInline,
               MovieVideoFilesAdmin, MovieSubscriptionInline)
    list_display = ('id', 'name', 'release_date', 'duration')
    exclude = ('countries', 'genres')


class MovieInline(admin.TabularInline):
    model = models.MovieSubscription.movies.through


class UserSubscriptionInline(admin.TabularInline):
    model = models.MovieSubscription.users.through


class MovieSubscriptionAdmin(admin.ModelAdmin):
    inlines = (MovieInline, UserSubscriptionInline,)
    list_display = ('id', 'name', 'price')
    exclude = ('movies', 'users',)


admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.MovieSubscription, MovieSubscriptionAdmin)
