from django.views.generic import DetailView
from .models import *
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import PortfolioForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.files.base import ContentFile

User = get_user_model()


@login_required
def add_portfolio(request):
    if request.method == 'GET':
        form = PortfolioForm()
        return render(request, 'services/add_portfolio.html', {'form': form})
    elif request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = Portfolio(user=request.user)
            portfolio.save()
            for f in request.FILES.getlist('images'):
                data = f.read()
                image = Image(portfolio=portfolio)
                image.image.save(f.name, ContentFile(data))
                image.save()
                return reverse('account:cabinet', kwargs={'pk': request.user.pk})
        else:
            return render(request, 'services/add_portfolio.html', {'form': form})


@login_required
def create_review(request):
    if request.method == 'POST':
        service_user_pk = request.POST.get('service_user_pk')
        client_user_pk = request.POST.get('client_user_pk')
        text = request.POST.get('text')
        service_user = User.objects.get(pk=service_user_pk)
        client_user = User.objects.get(pk=client_user_pk)
        if not Review.objects.filter(service_user=service_user, client_user=client_user).exists():
            review = Review(service_user=service_user, client_user=client_user, text=text)
            review.save()
            resp = {
                'success': True,
                'save': True
            }
        else:
            resp = {
                'success': True,
                'save': False,
            }
        return JsonResponse(resp, safe=False)
    else:
        return JsonResponse({'success': False}, safe=False)


class AgencyDetail(DetailView):
    model = Agency
    template_name = 'services/agency_detail.html'
    # context_object_name = 'agency'


class DanceDetail(DetailView):
    model = Dance
    template_name = 'services/dance_detail.html'
    # context_object_name = 'dance'


class PhotoStudioDetail(DetailView):
    model = PhotoStudio
    template_name = 'services/photostudio_detail.html'
    # context_object_name = 'photostudio'


class StylistDetail(DetailView):
    model = Stylist
    template_name = 'services/stylist_detail.html'
    # context_object_name = 'stylist'


class AccessoriesDetail(DetailView):
    model = Accessories
    template_name = 'services/accessories_detail.html'
    # context_object_name = 'accessories'


class CostumeDetail(DetailView):
    model = Costume
    template_name = 'services/costume_detail.html'
    # context_object_name = 'costume'


class DecorDetail(DetailView):
    model = Decor
    template_name = 'services/decor_detail.html'
    # context_object_name = 'decor'


class BouquetDetail(DetailView):
    model = Bouquet
    template_name = 'services/bouquet_detail.html'
    # context_object_name = 'bouquet'


class RingDetail(DetailView):
    model = Ring
    template_name = 'services/ring_detail.html'
    # context_object_name = 'ring'


class DressDetail(DetailView):
    model = Dress
    template_name = 'services/dress_detail.html'
    # context_object_name = 'dress'


class CakeDetail(DetailView):
    model = Cake
    template_name = 'services/cake_detail.html'
    # context_object_name = 'cake'


class InvitationDetail(DetailView):
    model = Invitation
    template_name = 'services/invitation_detail.html'
    # context_object_name = 'invitation'


class RegistryOfficeDetail(DetailView):
    model = RegistryOffice
    template_name = 'services/registryoffice_detail.html'
    # context_object_name = 'registryoffice'


class PresenterDetail(DetailView):
    model = Presenter
    template_name = 'services/presenter_detail.html'
    # context_object_name = 'presenter'


class MusicDetail(DetailView):
    model = Music
    template_name = 'services/music_detail.html'
    # context_object_name = 'music'


class TransportDetail(DetailView):
    model = Transport
    template_name = 'services/transport_detail.html'
    # context_object_name = 'transport'


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'services/artist_detail.html'
    # context_object_name = 'artist'


class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'services/restaurant_detail.html'
    # context_object_name = 'restaurant'


class PhotographerDetail(DetailView):
    model = Photographer
    template_name = 'services/photographer_detail.html'
    # context_object_name = 'photographer'

    def get_context_data(self, **kwargs):
        context = super(PhotographerDetail, self).get_context_data(**kwargs)
        if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
            context['reviewed'] = True
        context['reviews'] = Review.objects.all().filter(service_user=self.object.user)
        return context

