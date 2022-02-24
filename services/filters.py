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
    price = django_filters.RangeFilter(field_name='average_check')
    capacity = django_filters.RangeFilter()
    type = django_filters.ModelChoiceFilter(
        queryset=models.RestaurantType.objects.all(), empty_label='Тип заведения')
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )
    kitchen = django_filters.ModelMultipleChoiceFilter(
        queryset=models.KitchenType.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Restaurant
        fields = ['type', 'price', 'capacity', 'location']


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
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.PhotoStudio._TYPE, empty_label='Тип')
    price = django_filters.RangeFilter(field_name='price_per_hour')

    class Meta:
        model = models.PhotoStudio
        fields = ['type', 'price', 'location']


class DecorFilter(django_filters.FilterSet):
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )
    price = django_filters.RangeFilter()

    class Meta:
        model = models.Decor
        fields = ['location', 'price']


class TransportFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Transport._TYPE, empty_label='Тип')
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )
    car_type = django_filters.ModelChoiceFilter(
        queryset=models.CarType.objects.all(), empty_label='Тип авто')
    car_brand = django_filters.ModelMultipleChoiceFilter(
        queryset=models.CarBrand.objects.all(),
        widget=forms.SelectMultiple,
    )
    price = django_filters.RangeFilter()
    with_driver = django_filters.BooleanFilter(field_name='with_driver')

    class Meta:
        model = models.Transport
        fields = ['type', 'location', 'price', 'car_type', 'car_brand', 'with_driver']


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
    price = django_filters.RangeFilter(field_name='price_per_evening')
    composition = django_filters.ChoiceFilter(
        field_name='composition', choices=models.Music._COMPOSITION_TYPE, empty_label='Исполнители')
    language = django_filters.ModelMultipleChoiceFilter(
        queryset=models.Language.objects.all(),
        widget=forms.SelectMultiple
        )

    class Meta:
        model = models.Music
        fields = ['price', 'composition', 'language']


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
        field_name='type', choices=models.Costume._TYPE, empty_label='Тип')
    price = django_filters.RangeFilter()
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )
    condition = django_filters.ChoiceFilter(
        field_name='condition', choices=models.Costume._CONDITION_TYPES, empty_label='Вид сделки')

    class Meta:
        model = models.Costume
        fields = ['type', 'price', 'condition', 'location']


class RingFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Ring._TYPE, empty_label='Тип услуг')
    price = django_filters.RangeFilter()
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Ring
        fields = ['type', 'price', 'location']


class BouquetFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Bouquet._TYPE, empty_label='Тип')
    price = django_filters.RangeFilter()
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Bouquet
        fields = ['type', 'price', 'location']


class StylistFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Stylist._TYPE, empty_label='Тип')
    service_type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Stylist._SERVICE_TYPE, empty_label='Вид услуги')
    price = django_filters.RangeFilter()
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Stylist
        fields = ['type', 'price', 'service_type', 'location']


class DanceFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(
        field_name='type', choices=models.Dance._TYPE, empty_label='Тип')
    price = django_filters.RangeFilter()
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Dance
        fields = ['type', 'price', 'location']


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
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=District.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = models.Agency
        fields = ['location']
