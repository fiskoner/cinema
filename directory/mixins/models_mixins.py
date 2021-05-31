from django.db import models


class PersonDescription(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(default='', blank=True)
    date_birth = models.DateField(default=None, null=True, blank=True)

    class Meta:
        abstract = True
