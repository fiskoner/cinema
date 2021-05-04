from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework import permissions as rest_permissions, status, parsers
from rest_framework.response import Response

from core import pagination
from core.mixins.view_mixins import StaffEditPermissionViewSetMixin
from movies import serializers, models


class MovieViewSet(StaffEditPermissionViewSetMixin):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = (rest_permissions.IsAuthenticated, rest_permissions.IsAdminUser, )
    pagination_class = pagination.CustomPagination

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