from django import forms
from .models import Tender
from django.utils.translation import gettext_lazy as _


class TenderCreateForm(forms.ModelForm):
    on_date = forms.DateField(widget=forms.SelectDateWidget(), label=_("Дата события"))
    class Meta:
        model = Tender
        fields = ['service', 'on_date', 'budget', 'comment']


class TenderUpdateForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = ['on_date', 'budget', 'comment']
