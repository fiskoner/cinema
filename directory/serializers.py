from rest_framework import serializers
from directory import models


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Actor
        fields = '__all__'


class ActorMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ActorMovie
        fields = '__all__'


class MovieDirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MovieDirector
        fields = '__all__'


class MovieGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MovieGenre
        fields = '__all__'
