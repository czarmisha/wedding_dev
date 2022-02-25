from django.views.generic import DetailView
from django.core.files.base import ContentFile
from .models import *
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import PortfolioForm, VideoForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from django_filters.views import FilterView
from . import filters
from favorite.models import Favorite
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


User = get_user_model()


def agency_list(request):
    f = filters.AgencyFilter(request.GET, queryset=Agency.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/agency_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def dance_list(request):
    f = filters.DanceFilter(request.GET, queryset=Dance.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/dance_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def photostudio_list(request):
    f = filters.PhotoStudioFilter(request.GET, queryset=PhotoStudio.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/photostudio_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def stylist_list(request):
    f = filters.StylistFilter(request.GET, queryset=Stylist.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/stylist_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def accessories_list(request):
    f = filters.AccessoriesFilter(request.GET, queryset=Accessories.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    print(f.qs)
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/accessories_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def costume_list(request):
    f = filters.CostumeFilter(request.GET, queryset=Costume.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/costume_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def decor_list(request):
    f = filters.DecorFilter(request.GET, queryset=Decor.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/decor_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def bouquet_list(request):
    f = filters.BouquetFilter(request.GET, queryset=Bouquet.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/bouquet_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def ring_list(request):
    f = filters.RingFilter(request.GET, queryset=Ring.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/ring_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def dress_list(request):
    f = filters.DressFilter(request.GET, queryset=Dress.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/dress_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def cake_list(request):
    f = filters.CakeFilter(request.GET, queryset=Cake.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/cake_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def invitation_list(request):
    f = filters.InvitationFilter(request.GET, queryset=Invitation.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/invitation_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def registry_office_list(request):
    f = filters.RegistryOfficeFilter(request.GET, queryset=RegistryOffice.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/registryoffice_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def presenter_list(request):
    f = filters.PresenterFilter(request.GET, queryset=Presenter.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/presenter_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def music_list(request):
    f = filters.MusicFilter(request.GET, queryset=Music.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/music_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def transport_list(request):
    f = filters.TransportFilter(request.GET, queryset=Transport.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/transport_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def artist_list(request):
    f = filters.ArtistFilter(request.GET, queryset=Artist.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/artist_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def restaurant_list(request):
    f = filters.RestaurantFilter(request.GET, queryset=Restaurant.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/restaurant_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def photographer_list(request):
    f = filters.PhotographerFilter(request.GET, queryset=Photographer.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/photographer_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


def videographer_list(request):
    f = filters.VideographerFilter(request.GET, queryset=Videographer.objects.select_related(
        'user', 'user__portfolio').annotate(review_count=Count("user__service_reviews")).order_by('-is_pro', '-created'))
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page', 1)
    try:
        objs = paginator.page(page)
    except PageNotAnInteger:
        objs = paginator.page(1)
    except EmptyPage:
        objs = paginator.page(paginator.num_pages)

    return render(request, 'services/videographer_list.html', {
        'paginator': paginator,
        'filter': f,
        'objs': objs,
    })


@login_required
def add_portfolio(request):
    if request.method == 'GET':

        if request.user.type == 'transport':
            form = VideoForm()
        else:
            form = PortfolioForm()
        return render(request, 'services/add_portfolio.html', {'form': form})

    elif request.method == 'POST':

        if request.user.type == 'transport':
            form = VideoForm(request.POST, request.FILES)
        else:
            form = PortfolioForm(request.POST, request.FILES)

        if form.is_valid():
            portfolio = Portfolio(user=request.user)
            portfolio.save()
            if request.user.type == 'transport':
                for f in request.FILES.getlist('videos'):
                    data = f.read()
                    video = Video(portfolio=portfolio)
                    video.videofile.save(f.name, ContentFile(data))
                    video.save()
            else:
                for f in request.FILES.getlist('images'):
                    data = f.read()
                    image = Image(portfolio=portfolio)
                    image.image.save(f.name, ContentFile(data))
                    image.save()
            return HttpResponseRedirect(request.user.get_cabinet_url())
        else:
            return render(request, 'services/add_portfolio.html', {'form': form})
    else:
        return redirect('home')


@login_required
def extend_portfolio(request):
    if request.method == 'GET':
        form = PortfolioForm()
        return render(request, 'services/add_portfolio.html', {'form': form})
    elif request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = Portfolio.objects.get(user=request.user)
            for f in request.FILES.getlist('images'):
                data = f.read()
                image = Image(portfolio=portfolio)
                image.image.save(f.name, ContentFile(data))
                image.save()
            return HttpResponseRedirect(request.user.get_cabinet_url())
        else:
            return render(request, 'services/add_portfolio.html', {'form': form})
    else:
        return HttpResponseRedirect(request.user.get_cabinet_url())


@login_required
def delete_portfolio(request):
    portfolio = Portfolio.objects.get(user=request.user)
    if portfolio:
        portfolio.delete()
        return HttpResponseRedirect(request.user.get_cabinet_url())
    else:
        return HttpResponseRedirect(request.user.get_cabinet_url())


@login_required
def create_review(request):
    if request.method == 'POST':
        service_user_pk = request.POST.get('service_user_pk')
        client_user_pk = request.POST.get('client_user_pk')
        text = request.POST.get('text')
        rate_value = request.POST.get('rate_value')
        service_user = User.objects.get(pk=service_user_pk)
        client_user = User.objects.get(pk=client_user_pk)
        if not Review.objects.filter(service_user=service_user, client_user=client_user).exists():
            review = Review(service_user=service_user,
                            client_user=client_user, text=text, value=rate_value)
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class DanceDetail(DetailView):
    model = Dance
    template_name = 'services/dance_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class PhotoStudioDetail(DetailView):
    model = PhotoStudio
    template_name = 'services/photostudio_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class StylistDetail(DetailView):
    model = Stylist
    template_name = 'services/stylist_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class AccessoriesDetail(DetailView):
    model = Accessories
    template_name = 'services/accessories_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class CostumeDetail(DetailView):
    model = Costume
    template_name = 'services/costume_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class DecorDetail(DetailView):
    model = Decor
    template_name = 'services/decor_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class BouquetDetail(DetailView):
    model = Bouquet
    template_name = 'services/bouquet_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class RingDetail(DetailView):
    model = Ring
    template_name = 'services/ring_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class DressDetail(DetailView):
    model = Dress
    template_name = 'services/dress_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class CakeDetail(DetailView):
    model = Cake
    template_name = 'services/cake_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class InvitationDetail(DetailView):
    model = Invitation
    template_name = 'services/invitation_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class RegistryOfficeDetail(DetailView):
    model = RegistryOffice
    template_name = 'services/registryoffice_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class PresenterDetail(DetailView):
    model = Presenter
    template_name = 'services/presenter_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class MusicDetail(DetailView):
    model = Music
    template_name = 'services/music_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class TransportDetail(DetailView):
    model = Transport
    template_name = 'services/transport_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'services/artist_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'services/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class PhotographerDetail(DetailView):
    model = Photographer
    template_name = 'services/photographer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context


class VideographerDetail(DetailView):
    model = Videographer
    template_name = 'services/videographer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if Review.objects.filter(service_user=self.object.user, client_user=self.request.user).exists():
                context['reviewed'] = True
            if self.object.user.favorite_specialists.filter(client=self.request.user):
                context['favorite'] = True
        except:
            print('anonymous user')
        context['reviews'] = Review.objects.all().filter(
            service_user=self.object.user)
        return context
