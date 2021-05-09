# Generated by Django 3.2 on 2021-05-09 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0017_auto_20210509_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieUserPlayed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration_watched', models.DurationField(null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_played', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies_played', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='user_watched',
            field=models.ManyToManyField(related_name='movies_watched', through='movies.MovieUserPlayed', to=settings.AUTH_USER_MODEL),
        ),
    ]
