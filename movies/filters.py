from django_filters import rest_framework as rest_filters
from rest_framework import exceptions

from movies import models


class MovieFilter(rest_filters.FilterSet):
    year_from = rest_filters.NumberFilter(field_name='release_date', lookup_expr='year__gte')
    year_to = rest_filters.NumberFilter(field_name='release_date', lookup_expr='year__lte')
    duration_from = rest_filters.DurationFilter(method='filter_duration_from')
    duration_to = rest_filters.DurationFilter(method='filter_duration_to')
    ordering = rest_filters.OrderingFilter(
        fields=(
            ('id', 'id'), ('name', 'name'), ('release_date', 'date'), ('duration', 'duration')
        )
    )
    actors = rest_filters.CharFilter(method='filter_actors')
    genres = rest_filters.CharFilter(method='filter_genres')
    countries = rest_filters.CharFilter(method='filter_countries')
    watched = rest_filters.BooleanFilter(method='get_user_watched')

    class Meta:
        model = models.Movie
        fields = ('name', 'year_from', 'year_to', )

    def filter_duration_from(self, queryset, name, value):
        queryset = queryset.filter(duration__gte=value)
        return queryset

    def filter_duration_to(self, queryset, name, value):
        queryset = queryset.filter(duration__lte=value)
        return queryset

    def filter_actors(self, queryset, name, value):
        try:
            actors_list = list(map(int, value.split(',')))
        except ValueError:
            raise exceptions.ValidationError('Enter correct value')
        return queryset.filter(actors__actor_id__in=actors_list).distinct()

    def filter_genres(self, queryset, name, value):
        try:
            genres_list = list(map(int, value.split(',')))
        except ValueError:
            raise exceptions.ValidationError('Enter correct value')
        return queryset.filter(genres__in=genres_list).distinct()

    def filter_countries(self, queryset, name, value):
        try:
            countries_list = list(map(int, value.split(',')))
        except ValueError:
            raise exceptions.ValidationError('Enter correct value')
        return queryset.filter(countries__in=countries_list).distinct()

    def get_user_watched(self, queryset, name, value):
        user = self.request.user
        if user.is_anonymous:
            return queryset.all()
        if not value:
            return queryset.exclude(user_watched=user)
        return queryset.filter(user_watched=user)
