from django.urls import path
from . import views

app_name = 'favorite'
urlpatterns = [
    path('add/', views.add_to_favorite, name='add_to_favorite'),
]
