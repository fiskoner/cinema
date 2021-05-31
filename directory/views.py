import rest_framework.permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import permissions as rest_permissions
from core import permissions, pagination
from core.mixins import view_mixins
from directory import serializers, models, filters


class ActorViewSet(view_mixins.StaffEditPermissionViewSetMixin, view_mixins.FileParserViewSetMixin):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated, rest_framework.permissions.IsAdminUser)
    pagination_class = pagination.CustomPagination
    filterset_class = filters.ActorFilter

    @action(methods=['post'], detail=True)
    @swagger_auto_schema(request_body=serializers.ActorPhotoUploadSerializer)
    def upload_images(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')
        actor = self.get_object()
        bulk = [models.ActorPhoto(image=file, actor=actor) for file in files]
        models.ActorPhoto.objects.bulk_create(objs=bulk)
        serializer = self.serializer_class(actor)
        data = serializer.data
        return Response({'status': 'success', 'data': data}, status=status.HTTP_200_OK)


class ActorMovieViewSet(view_mixins.StaffEditPermissionViewSetMixin):
    queryset = models.ActorMovie.objects.all()
    serializer_class = serializers.ActorMovieSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated, rest_framework.permissions.IsAdminUser)
    pagination_class = pagination.CustomPagination


class MovieDirectorViewSet(view_mixins.StaffEditPermissionViewSetMixin, view_mixins.FileParserViewSetMixin):
    queryset = models.MovieDirector.objects.all()
    serializer_class = serializers.MovieDirectorSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated, rest_framework.permissions.IsAdminUser)
    pagination_class = pagination.CustomPagination
    filterset_class = filters.MovieDirectorFilter

    @action(methods=['post'], detail=True)
    @swagger_auto_schema(request_body=serializers.ActorPhotoUploadSerializer)
    def upload_images(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')
        movie_director = self.get_object()
        bulk = [models.MovieDirectorPhoto(image=file, movie_director=movie_director) for file in files]
        models.MovieDirectorPhoto.objects.bulk_create(objs=bulk)
        serializer = self.serializer_class(movie_director)
        data = serializer.data
        return Response({'status': 'success', 'data': data}, status=status.HTTP_200_OK)


class MovieGenreViewSet(view_mixins.StaffEditPermissionViewSetMixin):
    queryset = models.MovieGenre.objects.all()
    serializer_class = serializers.MovieGenreSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated, rest_framework.permissions.IsAdminUser)
    pagination_class = pagination.CustomPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return (rest_permissions.AllowAny(),)
        if self.action in ['update', 'create']:
            return (rest_permissions.IsAdminUser(),)
        return (permission() for permission in self.permission_classes)


class CountryViewSet(view_mixins.StaffEditPermissionViewSetMixin):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated, rest_framework.permissions.IsAdminUser)
    pagination_class = pagination.CustomPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return (rest_permissions.AllowAny(),)
        if self.action in ['update', 'create']:
            return (rest_permissions.IsAdminUser(),)
        return (permission() for permission in self.permission_classes)
