from django.urls import path
from . import views

app_name = 'tender'
urlpatterns = [
    path('list/', views.TenderList.as_view(), name='list'),
    path('create/', views.TenderCreate.as_view(), name='create'),
    path('detail/<slug:slug>', views.TenderDetail.as_view(), name='detail'),
    path('update/<slug:slug>', views.TenderUpdate.as_view(), name='update'),
    path('delete/<slug:slug>', views.TenderDelete.as_view(), name='delete'),
]