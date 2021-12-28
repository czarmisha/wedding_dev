from django import forms
from .models import Tender


class TenderCreateForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = ['service', 'on_date', 'budget', 'comment']
