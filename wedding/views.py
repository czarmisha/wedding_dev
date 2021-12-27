from django.shortcuts import render
from services.models import Photographer


def home(request):
    photographers = Photographer.objects.all()
    return render(request, 'wedding/home.html', context={'photographers': photographers})
