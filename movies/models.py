from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=255, default='', blank=True, verbose_name='Название фильма')
    release_date = models.DateField(null=True)
    duration = models.DurationField(null=True)
    description = models.TextField(default='', blank=True)
    rating = models.FloatField(null=True)

