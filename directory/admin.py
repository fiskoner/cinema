from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from directory import models
from directory.mixins.admin_mixins import ImageInlineMixin


class ActorPhotoInline(ImageInlineMixin):
    model = models.ActorPhoto


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'date_birth')
    inlines = (ActorPhotoInline,)


class MovieDirectorPhotoInline(ImageInlineMixin):
    model = models.MovieDirectorPhoto


class MovieDirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name' 'country', 'date_birth')
    inlines = (MovieDirectorPhotoInline)


# admin.site.register(models.Actor, ActorAdmin)
# admin.site.register(models.ActorMovie)
# admin.site.register(models.MovieDirector)
admin.site.register(models.MovieGenre)