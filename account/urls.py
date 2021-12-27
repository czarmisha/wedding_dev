from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('cabinet/<int:pk>', views.CabinetView.as_view(), name='cabinet'),
    path('login', views.user_login, name='login'),
    path('registration', views.user_register, name='registration'),
]