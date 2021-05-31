from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import User
from movies.models import MovieSubscription


class UserSubscriptionInline(admin.TabularInline):
    model = MovieSubscription.users.through


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    inlines = (UserSubscriptionInline,)
    model = User
