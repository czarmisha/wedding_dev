from django.urls import path
from . import views
from django.conf import settings

app_name = 'account'
urlpatterns = [
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('registration', views.user_register, name='registration'),
    path('cabinet/<int:pk>', views.CabinetView.as_view(), name='cabinet'),
    path('tenders/', views.my_tenders, name='tenders'),
    path('change-password/', views.change_password, name='change_password'),
    # path('cabinet/<slug:slug>/edit', views.ClientProfileUpdateView.as_view(), name='update_client_profile'),
    path('cabinet/edit', views.client_edit, name='update_client_profile'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('user-verify/<int:pk>/<str:token>', views.verify_email_confirm, name='verify_email_confirm'),
]
