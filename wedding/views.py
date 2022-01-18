from django.shortcuts import render
from tender.models import Tender


def home(request):
    tenders = Tender.objects.all()[:3]
    return render(request, 'wedding/home.html', context={'tenders': tenders})
