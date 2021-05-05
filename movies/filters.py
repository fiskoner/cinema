import datetime

from django_filters import rest_framework as rest_filters

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

    class Meta:
        model = models.Movie
        fields = ('name', 'year_from', 'year_to', )

    def filter_duration_from(self, queryset, name, value):
        queryset = queryset.filter(duration__gte=value)
        return queryset

    def filter_duration_to(self, queryset, name, value):
        queryset = queryset.filter(duration__lte=value)
        return queryset
