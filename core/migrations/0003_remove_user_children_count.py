# Generated by Django 3.2 on 2021-05-01 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='children_count',
        ),
    ]
