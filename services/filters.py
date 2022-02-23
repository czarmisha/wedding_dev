from queue import Empty
import django_filters
from django import forms
from . import models
from account.models import District


class PhotographerFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = models.Photographer
        fields = ['price']


class VideographerFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = models.Photographer
        fields = ['price']


class RestaurantFilter(django_filters.FilterSet):
    average_check_gt = django_filters.NumberFilter(
        field_name='average_check', lookup_expr='gte')
    average_check_lt = django_filters.NumberFilter(
        field_name='average_check', lookup_expr='lte')
    capacity_gt = django_filters.NumberFilter(
        field_name='capacity', lookup_expr='gte')
    capacity_lt = django_filters.NumberFilter(
        field_name='capacity', lookup_expr='lte')
    type = django_filters.ModelChoiceFilter(
        queryset=models.RestaurantType.objects.all())
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )
    kitchen = django_filters.ModelMultipleChoiceFilter(
        queryset=models.KitchenType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = models.Restaurant
        fields = ['type', 'average_check_gt', 'average_check_lt',
                  'capacity_gt', 'capacity_lt', 'location']


class RegistryOfficeFilter(django_filters.FilterSet):
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.RegistryOffice._REGISTRY_TYPE, empty_label='Виды регистрации')

    class Meta:
        model = models.RegistryOffice
        fields = ['type', 'location']


class PhotoStudioFilter(django_filters.FilterSet):
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )
    price_per_hour_lt = django_filters.NumberFilter(
        field_name='price_per_hour', lookup_expr='lte')
    price_per_hour_gt = django_filters.NumberFilter(
        field_name='price_per_hour', lookup_expr='gte')

    class Meta:
        model = models.PhotoStudio
        fields = ['location', 'price_per_hour_gt', 'price_per_hour_lt']


class DecorFilter(django_filters.FilterSet):
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')

    class Meta:
        model = models.Decor
        fields = ['location', 'price_gt', 'price_lt']


class TransportFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Transport._TYPE)
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )
    car_type = django_filters.ModelChoiceFilter(
        queryset=models.CarType.objects.all())
    car_brand = django_filters.ModelMultipleChoiceFilter(
        queryset=models.CarBrand.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    with_driver = django_filters.BooleanFilter(field_name='with_driver')

    class Meta:
        model = models.Transport
        fields = ['type', 'location', 'price_gt', 'price_lt',
                  'car_type', 'car_brand', 'with_driver']


class PresenterFilter(django_filters.FilterSet):
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    price_per_hour_lt = django_filters.NumberFilter(
        field_name='price_per_hour', lookup_expr='lte')
    price_per_hour_gt = django_filters.NumberFilter(
        field_name='price_per_hour', lookup_expr='gte')
    composition = django_filters.ChoiceFilter(
        field_name='composition', choices=models.Presenter._COMPOSITION_TYPE)
    gender = django_filters.ChoiceFilter(
        field_name='gender', choices=models.Presenter._GENDER)
    language = django_filters.ModelChoiceFilter(
        queryset=models.Language.objects.all())

    class Meta:
        model = models.Presenter
        fields = ['price_per_hour_gt', 'price_per_hour_lt',
                  'price_gt', 'price_lt', 'composition', 'gender', 'language']


class MusicFilter(django_filters.FilterSet):
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    price_per_evening_lt = django_filters.NumberFilter(
        field_name='price_per_evening', lookup_expr='lte')
    price_per_evening_gt = django_filters.NumberFilter(
        field_name='price_per_evening', lookup_expr='gte')
    composition = django_filters.ChoiceFilter(
        field_name='composition', choices=models.Music._COMPOSITION_TYPE)
    vocal = django_filters.ChoiceFilter(
        field_name='vocal', choices=models.Music._VOCAL_TYPE)
    language = django_filters.ModelChoiceFilter(
        queryset=models.Language.objects.all())

    class Meta:
        model = models.Music
        fields = ['price_per_evening_gt', 'price_per_evening_lt',
                  'price_gt', 'price_lt', 'composition', 'vocal', 'language']


class ArtistFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    type = django_filters.ModelChoiceFilter(
        queryset=models.ShowType.objects.all(), empty_label='Тип шоу')

    class Meta:
        model = models.Artist
        fields = ['price', 'type']


class CakeFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Cake._TYPES, empty_label='Тип услуг')
    price = django_filters.RangeFilter(field_name='price_per_kg')
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Cake
        fields = ['type', 'price', 'location']


class DressFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Dress._TYPE)
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )
    condition = django_filters.ChoiceFilter(
        field_name='condition', choices=models.Dress._CONDITION_TYPES)
    dress_type = django_filters.ChoiceFilter(
        field_name='dress_type', choices=models.Dress._DRESS_TYPES)

    class Meta:
        model = models.Dress
        fields = ['type', 'price_gt', 'price_lt',
                  'condition', 'dress_type', 'location']


class CostumeFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Costume._TYPE)
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )
    condition = django_filters.ChoiceFilter(
        field_name='condition', choices=models.Costume._CONDITION_TYPES)

    class Meta:
        model = models.Costume
        fields = ['type', 'price_gt', 'price_lt', 'condition', 'location']


class RingFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Ring._TYPE)
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Ring
        fields = ['type', 'price_gt', 'price_lt', 'location']


class BouquetFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Bouquet._TYPE)
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Bouquet
        fields = ['type', 'price_gt', 'price_lt', 'location']


class StylistFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Stylist._TYPE)
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Stylist
        fields = ['type', 'price_gt', 'price_lt', 'location']


class DanceFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Dance._TYPE)
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Dance
        fields = ['type', 'price_gt', 'price_lt', 'location']


class AccessoriesFilter(django_filters.FilterSet):
    accessories_type = django_filters.ModelChoiceFilter(
        queryset=models.AccessoriesType.objects.all(), empty_label='Тип')
    price = django_filters.RangeFilter()
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Accessories
        fields = ['accessories_type', 'location', 'price']


class InvitationFilter(django_filters.FilterSet):
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Invitation
        fields = ['location']


class AgencyFilter(django_filters.FilterSet):
    price_lt = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte')
    price_gt = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Agency
        fields = ['price_gt', 'price_lt', 'location']
