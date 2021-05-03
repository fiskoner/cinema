from django.contrib import admin

# Register your models here.
from movies import models

admin.site.register(models.Movie)