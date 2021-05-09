import datetime

from drf_yasg.utils import swagger_auto_schema
from rest_framework import parsers, status, mixins, exceptions
from rest_framework.decorators import action
from rest_framework import permissions as rest_permissions

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from core import pagination, permissions
from core.mixins.view_mixins import StaffEditPermissionViewSetMixin
from movies import serializers, models, filters, utils
from movies.models import UserMovieRating


class MovieViewSet(StaffEditPermissionViewSetMixin):
    queryset = models.Movie.objects.prefetch_related('user_watched').all()
    serializer_class = serializers.MovieSerializer
    # permission_classes = (rest_permissions.IsAuthenticated, rest_permissions.IsAdminUser, )
    permission_classes = (rest_permissions.AllowAny,)
    pagination_class = pagination.CustomPagination
    filterset_class = filters.MovieFilter

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return serializers.MovieDetailSerializer
        return self.serializer_class

    def get_parsers(self):
        if self.name == 'Upload images':
            return [parser() for parser in (parsers.MultiPartParser, parsers.FormParser)]
        return super().get_parsers()

    @action(methods=['post'], detail=True)
    @swagger_auto_schema(request_body=serializers.MoviePhotoUploadSerializer)
    def upload_images(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')
        movie = self.get_object()
        bulk = [models.MoviePhoto(image=file, movie=movie) for file in files]
        models.MoviePhoto.objects.bulk_create(objs=bulk)
        serializer = self.serializer_class(movie)
        data = serializer.data
        return Response({'status': 'success', 'data': data}, status=status.HTTP_200_OK)

    def stream_video(self, request, *args, **kwargs):
        file = kwargs.get('file')
        response = utils.stream_video(request=request, path=file)
        return response


class SetMovieRatingAPIView(GenericAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.SetMovieRatingSerializer
    permission_classes = (rest_permissions.IsAuthenticated, permissions.IsUserPermission)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        movie: models.Movie = self.get_object()
        UserMovieRating.objects.update_or_create(
            movie=movie,
            user=self.request.user,
            defaults={'rating': data.get('rating')}
        )
        return Response({'status': 'success', 'movie_rating': movie.rating}, status=status.HTTP_200_OK)


class SetMovieTimeWatchedAPIView(GenericAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.SetMovieTimeWatchedSerializer
    permission_classes = (rest_permissions.IsAuthenticated, permissions.IsUserPermission)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        movie: models.Movie = self.get_object()
        duration = datetime.datetime.strptime(data.get('duration'), '%H:%M:%S')
        duration_delta = datetime.timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)
        models.MovieUserPlayed.objects.update_or_create(
            movie=movie,
            user=self.request.user,
            defaults={'duration_watched': duration_delta}
        )
        return Response({'status': 'success', 'time_watched': movie.duration}, status=status.HTTP_200_OK)


class UserRatingsViewSet(GenericViewSet,
                         mixins.ListModelMixin):
    queryset = models.UserMovieRating.objects.all()
    serializer_class = serializers.MovieRatingSerializer
    permission_classes = (rest_permissions.IsAuthenticated, permissions.IsUserPermission)
    pagination_class = pagination.CustomPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
