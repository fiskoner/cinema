import rest_framework.permissions

from rest_framework.viewsets import ModelViewSet
from directory import models, serializers


class ActorViewSet(ModelViewSet):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)


class ActorMovieViewSet(ModelViewSet):
    queryset = models.ActorMovie.objects.all()
    serializer_class = serializers.ActorMovieSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)


class MovieDirectorViewSet(ModelViewSet):
    queryset = models.MovieDirector.objects.all()
    serializer_class = serializers.MovieDirectorSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)


class MovieGenreViewSet(ModelViewSet):
    queryset = models.MovieGenre.objects.all()
    serializer_class = serializers.MovieGenreSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)
