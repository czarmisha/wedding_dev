from django import forms


class PortfolioForm(forms.Form):
    files = forms.FileField(label='Фото/Видео', widget=forms.ClearableFileInput(attrs={'multiple': True}))


class VideoForm(forms.Form):
    videos = forms.FileField(label='Видео', widget=forms.ClearableFileInput(attrs={'multiple': True}))
