# Generated by Django 3.2 on 2021-05-03 13:27

import directory.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_auto_20210503_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDirectorPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=directory.models.MovieDirectorPhoto.get_images_upload_path)),
                ('movie_director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='directory.moviedirector')),
            ],
        ),
        migrations.CreateModel(
            name='ActorPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=directory.models.ActorPhoto.get_images_upload_path)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='directory.actor')),
            ],
        ),
    ]
