from django.contrib import admin

# Register your models here.
from directory.mixins.admin_mixins import ImageInlineMixin
from movies import models


class MoviePhotoInline(ImageInlineMixin):
    model = models.MoviePhoto


class MovieAdmin(admin.ModelAdmin):
    inlines = (MoviePhotoInline,)
    list_display = ('id', 'name', 'release_date', 'duration')


admin.site.register(models.Movie, MovieAdmin)
