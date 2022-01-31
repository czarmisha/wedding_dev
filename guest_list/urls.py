from django.urls import path
from . import views

app_name = 'guest_list'
urlpatterns = [
    path('', views.guest_list_view, name='guest_list'),
    path('save/', views.guest_save, name='guest_save'),
    path('del/', views.guest_delete, name='guest_delete'),
]