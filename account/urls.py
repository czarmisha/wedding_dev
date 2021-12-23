from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.SpecialistDetail.as_view(), name='specialist_detail'),
    path('cabinet/<int:pk>', views.CabinetView.as_view(), name='cabinet'),
    path('login', views.user_login, name='login'),
    path('registration', views.user_register, name='registration'),
]