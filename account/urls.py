from django.urls import path
from . import views
from django.conf import settings

app_name = 'account'
urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('registration', views.user_register, name='registration'),
    path('cabinet/<int:pk>', views.CabinetView.as_view(), name='cabinet'),
]
