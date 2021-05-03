import rest_framework.permissions
from rest_framework.viewsets import ModelViewSet

from core import permissions


class StaffEditPermissionViewSet(ModelViewSet):

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return rest_framework.permissions.IsAuthenticated(), permissions.IsUserPermission()
        return (permission() for permission in self.permission_classes)
