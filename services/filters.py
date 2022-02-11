from random import choices
import django_filters
from . import models
from account.models import District


class PhotographerFilter(django_filters.FilterSet):
    price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_per_hour_lt = django_filters.NumberFilter(field_name='price_per_hour', lookup_expr='lte')
    price_per_hour_gt = django_filters.NumberFilter(field_name='price_per_hour', lookup_expr='gte')

    class Meta:
        model = models.Photographer
        fields = ['price_gt', 'price_lt', 'price_per_hour_gt', 'price_per_hour_lt']


class RestaurantFilter(django_filters.FilterSet):
    average_check_gt = django_filters.NumberFilter(field_name='average_check', lookup_expr='gte')
    average_check_lt = django_filters.NumberFilter(field_name='average_check', lookup_expr='lte')
    capacity_gt = django_filters.NumberFilter(field_name='capacity', lookup_expr='gte')
    capacity_lt = django_filters.NumberFilter(field_name='capacity', lookup_expr='lte')
    type = django_filters.ModelChoiceFilter(queryset=models.RestaurantType.objects.all())
    location = django_filters.ModelChoiceFilter(queryset=District.objects.all())
    kitchen = django_filters.ModelMultipleChoiceFilter(queryset=models.KitchenType.objects.all())

    class Meta:
        model = models.Restaurant
        fields = ['type', 'average_check_gt', 'average_check_lt', 'capacity_gt', 'capacity_lt', 'location']


class RegistryOfficeFilter(django_filters.FilterSet):
    location = django_filters.ModelChoiceFilter(queryset=District.objects.all())
    type = django_filters.ChoiceFilter(field_name='type', choices=models.RegistryOffice._REGISTRY_TYPE)

    class Meta:
        model = models.RegistryOffice
        fields = ['type', 'location' ]

