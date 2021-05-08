# Generated by Django 3.2 on 2021-05-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0010_alter_actormovie_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actorphoto',
            name='is_title',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='moviedirectorphoto',
            name='is_title',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='actorphoto',
            unique_together={('actor', 'is_title')},
        ),
        migrations.AlterUniqueTogether(
            name='moviedirectorphoto',
            unique_together={('movie_director', 'is_title')},
        ),
    ]
