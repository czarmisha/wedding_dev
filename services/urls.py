from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('photographer/<slug:slug>', views.PhotographerDetail.as_view(), name='photographer_detail'),
    path('restaurant/<slug:slug>', views.RestaurantDetail.as_view(), name='restaurant_detail'),
    path('artist/<slug:slug>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('transport/<slug:slug>', views.TransportDetail.as_view(), name='transport_detail'),
    path('music/<slug:slug>', views.MusicDetail.as_view(), name='music_detail'),
    path('presenter/<slug:slug>', views.PresenterDetail.as_view(), name='presenter_detail'),
    path('registry-office/<slug:slug>', views.RegistryOfficeDetail.as_view(), name='registryoffice_detail'),
    path('invitations/<slug:slug>', views.InvitationDetail.as_view(), name='invitation_detail'),
    path('cakes/<slug:slug>', views.CakeDetail.as_view(), name='cake_detail'),
    path('dresses/<slug:slug>', views.DressDetail.as_view(), name='dress_detail'),
    path('rings/<slug:slug>', views.RingDetail.as_view(), name='ring_detail'),
    path('bouquet/<slug:slug>', views.BouquetDetail.as_view(), name='bouquet_detail'),
    path('decor/<slug:slug>', views.DecorDetail.as_view(), name='decor_detail'),
    path('costumes/<slug:slug>', views.CostumeDetail.as_view(), name='costume_detail'),
    path('accessories/<slug:slug>', views.AccessoriesDetail.as_view(), name='accessories_detail'),
    path('stylist/<slug:slug>', views.StylistDetail.as_view(), name='stylist_detail'),
    path('photo-studio/<slug:slug>', views.PhotoStudioDetail.as_view(), name='photostudio_detail'),
    path('dance/<slug:slug>', views.DanceDetail.as_view(), name='dance_detail'),
    path('agency/<slug:slug>', views.AgencyDetail.as_view(), name='agency_detail'),
    path('create-review/', views.create_review, name='create_review'),
]