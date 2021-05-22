from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    model = User
