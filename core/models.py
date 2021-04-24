from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    class UserTypeChoices(models.TextChoices):
        user = 'User', 'Пользователь'
        admin = 'Admin', 'Администратор'

    class GenderChoices(models.TextChoices):
        male = 'Male', 'Мужчина'
        female = 'Female', 'Женщина'

    user_type = models.CharField(
        max_length=50, choices=UserTypeChoices.choices, default=UserTypeChoices.user, verbose_name='Тип юзера'
    )
    phone = models.CharField(max_length=20, default='', blank=True, verbose_name='Телефон')
    description = models.TextField(default='', blank=True, verbose_name='Описание')
    date_birth = models.DateField(null=True, blank=True, verbose_name='День рождения')
    discount = models.FloatField(null=True, verbose_name='Скидка')
    children_count = models.IntegerField(null=True, verbose_name='Количество детей')
