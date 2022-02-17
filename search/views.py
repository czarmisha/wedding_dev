from django.shortcuts import render
from django.db.models import Q
from services.models import *


def search_service(request):
    if request.method == 'GET':
        service = request.GET.get('service')
        name = request.GET.get('name')
        print(name, service)
        if not service or not name:
            print('not serv or name', request)
            return render(request, 'search/search_result.html', {
                'error': 'Произошла какая-то ошибка. Проверьте вводимые данные перед отправкой'
                })
        if service == 'photographer':
            queryset = Photographer.objects.filter(Q(name__icontains=name))
        elif service == 'videographer':
            queryset = Videographer.objects.filter(Q(name__icontains=name))
        elif service == 'restaurant':
            queryset = Restaurant.objects.filter(Q(name__icontains=name))
        elif service == 'artist':
            queryset = Artist.objects.filter(Q(name__icontains=name))
        elif service == 'transport':
            queryset = Transport.objects.filter(Q(name__icontains=name))
        elif service == 'music':
            queryset = Music.objects.filter(Q(name__icontains=name))
        elif service == 'presenter':
            queryset = Presenter.objects.filter(Q(name__icontains=name))
        elif service == 'registryoffice':
            queryset = RegistryOffice.objects.filter(Q(name__icontains=name))
        elif service == 'invitation':
            queryset = Invitation.objects.filter(Q(name__icontains=name))
        elif service == 'cake':
            queryset = Cake.objects.filter(Q(name__icontains=name))
        elif service == 'dress':
            queryset = Dress.objects.filter(Q(name__icontains=name))
        elif service == 'ring':
            queryset = Ring.objects.filter(Q(name__icontains=name))
        elif service == 'bouquet':
            queryset = Bouquet.objects.filter(Q(name__icontains=name))
        elif service == 'decor':
            queryset = Decor.objects.filter(Q(name__icontains=name))
        elif service == 'costume':
            queryset = Costume.objects.filter(Q(name__icontains=name))
        elif service == 'accessories':
            queryset = Accessories.objects.filter(Q(name__icontains=name))
        elif service == 'stylist':
            queryset = Stylist.objects.filter(Q(name__icontains=name))
        elif service == 'photostudio':
            queryset = PhotoStudio.objects.filter(Q(name__icontains=name))
        elif service == 'dance':
            queryset = Dance.objects.filter(Q(name__icontains=name))
        elif service == 'agency':
            queryset = Agency.objects.filter(Q(name__icontains=name))

        queryset = 'Поиск не дал никаких результатов' if not queryset else queryset
        print(queryset, 'asd')
        return render(request, 'search/search_result.html', {
                'queryset': queryset,
                })
