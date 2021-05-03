from django.contrib import admin

# Register your models here.
from directory import models

admin.site.register(models.Actor)
admin.site.register(models.ActorMovie)
admin.site.register(models.MovieDirector)
admin.site.register(models.MovieGenre)