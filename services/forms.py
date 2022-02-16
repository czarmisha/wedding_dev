from django import forms


class PortfolioForm(forms.Form):
    images = forms.ImageField(label='Фотографии', widget=forms.ClearableFileInput(attrs={'multiple': True}))


class VideoForm(forms.Form):
    videos = forms.FileField(label='Видео', widget=forms.ClearableFileInput(attrs={'multiple': True}))
