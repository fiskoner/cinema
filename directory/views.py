import rest_framework.permissions

from core import permissions
from core.mixins import view_mixins
from directory import serializers, models


class ActorViewSet(view_mixins.StaffEditPermissionViewSet):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated, permissions.IsAdminPermission)


class ActorMovieViewSet(view_mixins.StaffEditPermissionViewSet):
    queryset = models.ActorMovie.objects.all()
    serializer_class = serializers.ActorMovieSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated, permissions.IsAdminPermission)


class MovieDirectorViewSet(view_mixins.StaffEditPermissionViewSet):
    queryset = models.MovieDirector.objects.all()
    serializer_class = serializers.MovieDirectorSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated, permissions.IsAdminPermission)


class MovieGenreViewSet(view_mixins.StaffEditPermissionViewSet):
    queryset = models.MovieGenre.objects.all()
    serializer_class = serializers.MovieGenreSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated, permissions.IsAdminPermission)
