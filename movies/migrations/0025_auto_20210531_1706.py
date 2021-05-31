# Generated by Django 3.2 on 2021-05-31 17:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0024_auto_20210529_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movietousersubscription',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата подписания'),
        ),
        migrations.AlterField(
            model_name='movietousersubscription',
            name='time_end',
            field=models.DateTimeField(null=True, verbose_name='Дата окончания подписки'),
        ),
    ]