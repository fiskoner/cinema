from django.utils import timezone
from rest_framework import serializers, exceptions

from directory.models import Country
from directory import serializers as directory_serializers
from movies import models
from movies.models import MovieSubscription


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


class MovieSubscriptionSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField(method_name='check_user_subscribed')
    time_end = serializers.SerializerMethodField()

    class Meta:
        model = models.MovieSubscription
        fields = ('id', 'name', 'is_subscribed', 'time_end',)

    def get_time_end(self, instance: models.MovieSubscription):
        user = self.context.get('request').user
        if user.is_anonymous:
            return None
        subscription = instance.subscription_users.filter(user=user, subscription=instance)
        if subscription.exists():
            return subscription.first().time_end.strftime('%Y-%m-%d %H:%M:%S')
        return None

    def check_user_subscribed(self, instance: models.MovieSubscription):
        user = self.context.get('request').user
        return user in instance.users.all()


class MovieSerializer(serializers.ModelSerializer):
    photos = MoviePhotoUploadSerializer(many=True, read_only=True)
    countries = MovieCountrySerializer(many=True)
    genres = MovieInGenreSerializer(many=True)
    time_watched = serializers.SerializerMethodField(method_name='get_time_watched')
    subscriptions = MovieSubscriptionSerializer(many=True, required=False)
    user_rating = serializers.SerializerMethodField()
    user_rated_count = serializers.IntegerField()
    subscription_active = serializers.SerializerMethodField(method_name='check_subscription')

    class Meta:
        model = models.Movie
        exclude = ('user_rated', )
        include = ('user_rating', )

    def get_time_watched(self, instance: models.Movie):
        user = self.context.get('request').user
        if user.is_anonymous:
            return None
        time_watched = instance.users_played.filter(user=user)
        if time_watched.exists():
            return time_watched.first().duration_watched
        return None

    def get_user_rating(self, instance: models.Movie):
        user = self.context.get('request').user
        if user.is_anonymous:
            return None
        user_rating = models.UserMovieRating.objects.filter(user=user, movie=instance)
        if not user_rating.exists():
            return None
        return user_rating.first().rating

    def check_subscription(self, instance: models.Movie):
        user = self.context.get('request').user
        if user.is_anonymous and instance.subscriptions.exists():
            return 'Please register subscription for watching this movie'
        elif user.is_anonymous:
            return None
        movie_in_subscription = MovieSubscription.objects.filter(movies=instance)
        if not movie_in_subscription.exists():
            return None
        user_subscription = movie_in_subscription.filter(users=user, movies=instance)
        if not user_subscription.exists():
            return 'Please register subscription for watching this movie'
        user_subscription: MovieSubscription = movie_in_subscription.first()
        if user_subscription.subscription_users.get(user=user,
                                                    subscription=user_subscription).time_end < timezone.now():
            return 'Your subscription ended, please subscribe again to watch this movie'
        return None


class MovieSubscriptionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        models = models.MovieSubscription
        fields = '__all__'


class SetMovieRatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField()


class SetMovieTimeWatchedSerializer(serializers.Serializer):
    duration = serializers.DurationField()


class MovieRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserMovieRating
        exclude = ('id', 'user',)


class MovieVideoFiles(serializers.ModelSerializer):
    video_360p = serializers.BooleanField(source='video_360p_exists')
    video_480p = serializers.BooleanField(source='video_480p_exists')
    video_720p = serializers.BooleanField(source='video_720p_exists')

    class Meta:
        model = models.MovieVideoFiles
        fields = ('video_360p', 'video_480p', 'video_720p')


class MovieDetailSerializer(MovieSerializer):
    actors = directory_serializers.ActorMovieSerializer(many=True)
    directors = directory_serializers.MovieDirectorSerializer(many=True)
    videos = MovieVideoFiles(read_only=True)

    class Meta:
        model = models.Movie
        fields = '__all__'
        include = ('actors',)
