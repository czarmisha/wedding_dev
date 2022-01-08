import django_filters
from . import models


class PhotographerFilter(django_filters.FilterSet):
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_per_hour_lt = django_filters.NumberFilter(field_name='price_per_hour', lookup_expr='lte')
    price_per_hour_gt = django_filters.NumberFilter(field_name='price_per_hour', lookup_expr='gte')

    class Meta:
        model = models.Photographer
        fields = ['price_gt', 'price_lt', 'price_per_hour_gt', 'price_per_hour_lt']

