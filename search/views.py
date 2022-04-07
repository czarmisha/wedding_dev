from django.shortcuts import render
from django.db.models import Q, Count
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
            queryset = Photographer.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'videographer':
            queryset = Videographer.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'restaurant':
            queryset = Restaurant.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'artist':
            queryset = Artist.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'transport':
            queryset = Transport.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'music':
            queryset = Music.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'presenter':
            queryset = Presenter.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'registryoffice':
            queryset = RegistryOffice.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'invitation':
            queryset = Invitation.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'cake':
            queryset = Cake.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'dress':
            queryset = Dress.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'ring':
            queryset = Ring.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'bouquet':
            queryset = Bouquet.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'decor':
            queryset = Decor.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'costume':
            queryset = Costume.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'accessories':
            queryset = Accessories.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'stylist':
            queryset = Stylist.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'photostudio':
            queryset = PhotoStudio.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'dance':
            queryset = Dance.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')
        elif service == 'agency':
            queryset = Agency.objects.filter(Q(name__icontains=name)).filter(
            user__portfolio__isnull=False).select_related('user', 'user__portfolio').annotate(
            review_count=Count("user__service_reviews")).order_by('-is_pro', '-created')

        queryset = 'Поиск не дал никаких результатов' if not queryset else queryset
        print(queryset, 'asd')
        return render(request, 'search/search_result.html', {
                'queryset': queryset,
                })
