# Generated by Django 3.2 on 2021-05-05 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_movie_genres'),
        ('directory', '0009_moviedirectorphoto_is_title'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='actormovie',
            unique_together={('movie', 'actor')},
        ),
    ]
