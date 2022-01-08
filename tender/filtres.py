import django_filters
from .models import Tender
from django.forms import DateInput


class TenderFilter(django_filters.FilterSet):
    budget_gt = django_filters.NumberFilter(field_name='budget', lookup_expr='gte')
    budget_lt = django_filters.NumberFilter(field_name='budget', lookup_expr='lte')
    on_date_start = django_filters.DateFilter(field_name='on_date', lookup_expr='lte',
                                              widget=DateInput(attrs={'type': 'date',
                                                                      'placeholder': 'мм/дд/гг'}))
    on_date_end = django_filters.DateFilter(field_name='on_date', lookup_expr='gte',
                                            widget=DateInput(attrs={'type': 'date',
                                                                    'placeholder': 'мм/дд/гг'}))

    class Meta:
        model = Tender
        fields = ['service']
