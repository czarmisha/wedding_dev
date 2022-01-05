from django import forms


class PortfolioForm(forms.Form):
    images = forms.ImageField(label='Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))

