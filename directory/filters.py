from django_filters import rest_framework as rest_filters

from directory import models


class ActorFilter(rest_filters.FilterSet):
    birth_year_from = rest_filters.NumberFilter(field_name='date_birth', lookup_expr='year__gte')
    birth_year_to = rest_filters.NumberFilter(field_name='date_birth', lookup_expr='year__lte')
    ordering = rest_filters.OrderingFilter(
        fields=(
            ('id', 'id'), ('name', 'name'), ('date_birth', 'date_birth')
        )
    )

    class Meta:
        model = models.Actor
        fields = ('name', 'birth_year_from', 'birth_year_to', 'country')


class MovieDirectorFilter(rest_filters.FilterSet):
    birth_year_from = rest_filters.NumberFilter(field_name='date_birth', lookup_expr='year__gte')
    birth_year_to = rest_filters.NumberFilter(field_name='date_birth', lookup_expr='year__lte')

    class Meta:
        model = models.MovieDirector
        fields = ('name', 'birth_year_from', 'birth_year_to', 'country')