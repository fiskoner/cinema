from rest_framework import serializers

from directory.models import Country
from directory import serializers as directory_serializers
from movies import models


class MoviePhotoUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(source='image')

    class Meta:
        model = models.MoviePhoto
        fields = ('file', 'is_title')


class MovieCountrySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class MovieInGenreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class MovieSerializer(serializers.ModelSerializer):
    photos = MoviePhotoUploadSerializer(many=True, read_only=True)
    countries = MovieCountrySerializer(many=True)
    genres = MovieInGenreSerializer(many=True)

    class Meta:
        model = models.Movie
        fields = '__all__'


class MovieDetailSerializer(MovieSerializer):
    actors = directory_serializers.ActorMovieSerializer(many=True)

    class Meta:
        model = models.Movie
        fields = '__all__'
        include = ('actors',)
