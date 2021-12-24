from django.urls import path
from . import views

urlpatterns = [
    path('photographer/<slug:slug>', views.PhotographerDetail.as_view(), name='photographer_detail'),
    path('cabinet/<int:pk>', views.CabinetView.as_view(), name='cabinet'),
    path('login', views.user_login, name='login'),
    path('registration', views.user_register, name='registration'),
]