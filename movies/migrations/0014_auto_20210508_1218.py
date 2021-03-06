# Generated by Django 3.2 on 2021-05-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_auto_20210508_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviephoto',
            name='is_title',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='moviephoto',
            unique_together={('movie', 'is_title')},
        ),
    ]
