from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework import permissions as rest_permissions, status, parsers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from core import pagination, permissions
from core.mixins.view_mixins import StaffEditPermissionViewSetMixin
from movies import serializers, models, filters
from movies.models import UserMovieRating


class MovieViewSet(StaffEditPermissionViewSetMixin):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = (rest_permissions.IsAuthenticated, rest_permissions.IsAdminUser, )
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


class SetMovieRatingApiView(GenericAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieRatingSerializer
    permission_classes = (rest_permissions.IsAuthenticated, permissions.IsUserPermission)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        movie = self.get_object()
        UserMovieRating.objects.update_or_create(
            movie=movie,
            user=self.request.user,
            defaults={'rating': data.get('rating')}
        )
        return Response({'status': 'success', 'movie_rating': movie.rating}, status=status.HTTP_200_OK)