from django.views.generic import DetailView
from .models import *


def create_review(request):
    #TODO create view for review
    pass


class AgencyDetail(DetailView):
    model = Agency
    template_name = 'services/agency_detail.html'
    context_object_name = 'agency'


class DanceDetail(DetailView):
    model = Dance
    template_name = 'services/dance_detail.html'
    context_object_name = 'dance'


class PhotoStudioDetail(DetailView):
    model = PhotoStudio
    template_name = 'services/photostudio_detail.html'
    context_object_name = 'photostudio'


class StylistDetail(DetailView):
    model = Stylist
    template_name = 'services/stylist_detail.html'
    context_object_name = 'stylist'


class AccessoriesDetail(DetailView):
    model = Accessories
    template_name = 'services/accessories_detail.html'
    context_object_name = 'accessories'


class CostumeDetail(DetailView):
    model = Costume
    template_name = 'services/costume_detail.html'
    context_object_name = 'costume'


class DecorDetail(DetailView):
    model = Decor
    template_name = 'services/decor_detail.html'
    context_object_name = 'decor'


class BouquetDetail(DetailView):
    model = Bouquet
    template_name = 'services/bouquet_detail.html'
    context_object_name = 'bouquet'


class RingDetail(DetailView):
    model = Ring
    template_name = 'services/ring_detail.html'
    context_object_name = 'ring'


class DressDetail(DetailView):
    model = Dress
    template_name = 'services/dress_detail.html'
    context_object_name = 'dress'


class CakeDetail(DetailView):
    model = Cake
    template_name = 'services/cake_detail.html'
    context_object_name = 'cake'


class InvitationDetail(DetailView):
    model = Invitation
    template_name = 'services/invitation_detail.html'
    context_object_name = 'invitation'


class RegistryOfficeDetail(DetailView):
    model = RegistryOffice
    template_name = 'services/registryoffice_detail.html'
    context_object_name = 'registryoffice'


class PresenterDetail(DetailView):
    model = Presenter
    template_name = 'services/presenter_detail.html'
    context_object_name = 'presenter'


class MusicDetail(DetailView):
    model = Music
    template_name = 'services/music_detail.html'
    context_object_name = 'music'


class TransportDetail(DetailView):
    model = Transport
    template_name = 'services/transport_detail.html'
    context_object_name = 'transport'


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'services/artist_detail.html'
    context_object_name = 'artist'


class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'services/restaurant_detail.html'
    context_object_name = 'restaurant'


class PhotographerDetail(DetailView):
    model = Photographer
    template_name = 'services/photographer_detail.html'
    context_object_name = 'photographer'

