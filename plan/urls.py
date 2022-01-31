from django.urls import path
from . import views

app_name = 'plan'
urlpatterns = [
    path('', views.plan_view, name='plan_list'),
    path('save/', views.plan_save, name='plan_save'),
    path('del/', views.plan_delete, name='plan_delete'),
]