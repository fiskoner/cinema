# Generated by Django 3.2 on 2021-05-31 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0013_alter_moviedirector_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='date_birth',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='moviedirector',
            name='date_birth',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
