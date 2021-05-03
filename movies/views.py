from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions as rest_permissions

from core import permissions
from core.mixins.view_mixins import StaffEditPermissionViewSet
from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(StaffEditPermissionViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (rest_permissions.IsAuthenticated, rest_permissions.IsAdminUser, )
