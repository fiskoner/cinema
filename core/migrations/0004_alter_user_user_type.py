# Generated by Django 3.2 on 2021-05-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_user_children_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('User', 'Пользователь'), ('Admin', 'Администратор'), ('Director', 'Директор')], default='User', max_length=50, verbose_name='Тип юзера'),
        ),
    ]