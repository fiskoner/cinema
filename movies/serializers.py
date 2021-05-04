from rest_framework import serializers

from directory.models import Country
from movies import models


class MoviePhotoUploadSerializer(serializers.ModelSerializer):
    file = serializers.FileField(source='image')

    class Meta:
        model = models.MoviePhoto
        fields = ('file',)


class MovieSerializer(serializers.ModelSerializer):
    photos = MoviePhotoUploadSerializer(many=True, read_only=True)
    countries = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all(), many=True, required=False)

    class Meta:
        model = models.Movie
        fields = '__all__'
