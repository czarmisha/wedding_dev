from django.urls import path
from . import views

app_name = 'budget'
urlpatterns = [
    path('', views.budget_view, name='budget_view'),
    path('save/', views.budget_save, name='budget_save'),
]
