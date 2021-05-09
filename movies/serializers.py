from rest_framework import serializers

from directory.models import Country
from directory import serializers as directory_serializers
from movies import models


class MoviePhotoUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(source='image')

    class Meta:
        model = models.MoviePhoto
        fields = ('file', 'is_title')


class MovieStreamSerializer(serializers.Serializer):
    url = serializers.IntegerField()


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
    time_watched = serializers.SerializerMethodField(method_name='get_time_watched')

    class Meta:
        model = models.Movie
        fields = '__all__'

    def get_time_watched(self, instance: models.Movie):
        user = self.context.get('request').user
        time_watched = instance.users_played.filter(user=user)
        if time_watched.exists():
            return time_watched.first().duration_watched
        return None


class SetMovieRatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField()


class SetMovieTimeWatchedSerializer(serializers.Serializer):
    duration = serializers.DurationField()


class MovieRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserMovieRating
        exclude = ('id', 'user',)


class MovieVideoFiles(serializers.ModelSerializer):
    video_360p = serializers.FileField(use_url=False)
    video_480p = serializers.FileField(use_url=False)
    video_720p = serializers.FileField(use_url=False)

    class Meta:
        model = models.MovieVideoFiles
        exclude = ('id', 'movie')


class MovieDetailSerializer(MovieSerializer):
    actors = directory_serializers.ActorMovieSerializer(many=True)
    videos = MovieVideoFiles(read_only=True)

    class Meta:
        model = models.Movie
        fields = '__all__'
        include = ('actors',)
