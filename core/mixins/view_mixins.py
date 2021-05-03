import rest_framework.permissions
from rest_framework import parsers
from rest_framework.viewsets import ModelViewSet

from core import permissions


class StaffEditPermissionViewSetMixin(ModelViewSet):

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return rest_framework.permissions.IsAuthenticated(), permissions.IsUserPermission()
        print(self.permission_classes)
        return (permission() for permission in self.permission_classes)


class FileParserViewSetMixin(ModelViewSet):

    def get_parsers(self):
        if self.name == 'Upload images':
            return [parser() for parser in (parsers.MultiPartParser, parsers.FormParser)]
        return super().get_parsers()