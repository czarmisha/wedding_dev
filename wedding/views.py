from django.shortcuts import render
from tender.models import Tender


def home(request):
    tenders = Tender.objects.all()[:3]
    return render(request, 'wedding/home.html', context={'tenders': tenders})

def promo(request):
    return render(request, 'wedding/promo.html', context={})

def catalog(request):
    return render(request, 'services/catalog.html', context={})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
    