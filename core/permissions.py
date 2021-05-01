from rest_framework import permissions

from core.models import User


class IsUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == User.UserTypeChoices.user


class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == User.UserTypeChoices.admin


class IsDirectorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == User.UserTypeChoices.director
