from rest_framework import serializers
from directory import models


class ActorPhotoUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(source='image')

    class Meta:
        model = models.ActorPhoto
        fields = ('file', )


class ActorSerializer(serializers.ModelSerializer):
    photos = ActorPhotoUploadSerializer(many=True, read_only=True)

    class Meta:
        model = models.Actor
        fields = '__all__'


class ActorMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ActorMovie
        fields = '__all__'


class MovieDirectorPhotoUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(source='image')

    class Meta:
        model = models.MovieDirectorPhoto
        fields = ('file',)


class MovieDirectorSerializer(serializers.ModelSerializer):
    photos = MovieDirectorPhotoUploadSerializer(many=True, read_only=True)

    class Meta:
        model = models.MovieDirector
        fields = '__all__'


class MovieGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MovieGenre
        fields = '__all__'
