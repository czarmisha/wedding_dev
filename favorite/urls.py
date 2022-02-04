from django.urls import path
from . import views

app_name = 'favorite'
urlpatterns = [
    path('add/', views.add_to_favorite, name='add_to_favorite'),
    path('remove/', views.remove_from_favorite, name='remove_from_favorite'),
    path('', views.my_favorites, name='my_favorites'),
]
