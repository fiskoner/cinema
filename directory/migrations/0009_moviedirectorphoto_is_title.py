# Generated by Django 3.2 on 2021-05-04 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0008_alter_actorphoto_is_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedirectorphoto',
            name='is_title',
            field=models.BooleanField(null=True, unique=True),
        ),
    ]
