from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Favorite
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def add_to_favorite(request):
    if request.method == 'POST':
        service_pk = request.POST.get('service_pk')
        specialist = User.objects.filter(pk=service_pk).first()
        success = False
        err = ''
        if request.user.type == 'client':
            favorite = Favorite.objects.filter(client=request.user, specialist=specialist).first()
            if not favorite:
                favorite = Favorite(client=request.user, specialist=specialist)
                favorite.save()
                success = True
        else:
            err = 'Эта услуга доступна только для молодоженов'

        resp = {
            'success': success,
            'error': err,
        }
        return JsonResponse(resp, safe=False)
    else:
        return JsonResponse({'success': False}, safe=False)


@login_required
def remove_from_favorite(request):
    if request.method == 'POST':
        service_pk = request.POST.get('service_pk')
        specialist = User.objects.filter(pk=service_pk).first()
        success = False
        err = ''
        if request.user.type == 'client':
            favorite = Favorite.objects.filter(client=request.user, specialist=specialist).first()
            if favorite:
                favorite.delete()
                success = True
        else:
            err = 'Эта услуга доступна только для молодоженов'

        resp = {
            'success': success,
            'error': err,
        }
        return JsonResponse(resp, safe=False)
    else:
        return JsonResponse({'success': False}, safe=False)


@login_required
def my_favorites(request):
    if request.user.type != 'client':
        return 'error message todo'

    all_favorites_for_client = Favorite.objects.filter(client=request.user).all()
    favorites_count = all_favorites_for_client.count()
    context = {
        'photographers': [],
        'restaurants': [],
        'artists': [],
        'transport': [],
        'music': [],
        'presenters': [],
        'registry_offices': [],
        'invitations': [],
        'cakes': [],
        'dresses': [],
        'rings': [],
        'bouquets': [],
        'decor': [],
        'costumes': [],
        'accessories': [],
        'stylists': [],
        'photostudios': [],
        'dance': [],
        'agencies': [],
        'videographers': [],
        'count': favorites_count
    }

    for favorite in all_favorites_for_client:
        if favorite.specialist.type == 'photographer':
            context['photographers'].append(favorite.specialist.photographer)
        elif favorite.specialist.type == 'restaurant':
            context['restaurants'].append(favorite.specialist.restaurant)
        elif favorite.specialist.type == 'registryoffice':
            context['registry_offices'].append(favorite.specialist.registryoffice)
        elif favorite.specialist.type == 'artist':
            context['artists'].append(favorite.specialist.artist)
        elif favorite.specialist.type == 'transport':
            context['transport'].append(favorite.specialist.transport)
        elif favorite.specialist.type == 'music':
            context['music'].append(favorite.specialist.music)
        elif favorite.specialist.type == 'presenter':
            context['presenters'].append(favorite.specialist.presenter)
        elif favorite.specialist.type == 'invitation':
            context['invitations'].append(favorite.specialist.registryofinvitationfice)
        elif favorite.specialist.type == 'cake':
            context['cakes'].append(favorite.specialist.cake)
        elif favorite.specialist.type == 'dress':
            context['dresses'].append(favorite.specialist.dress)
        elif favorite.specialist.type == 'ring':
            context['rings'].append(favorite.specialist.ring)
        elif favorite.specialist.type == 'bouquet':
            context['bouquets'].append(favorite.specialist.bouquet)
        elif favorite.specialist.type == 'decor':
            context['decor'].append(favorite.specialist.decor)
        elif favorite.specialist.type == 'costume':
            context['costumes'].append(favorite.specialist.costume)
        elif favorite.specialist.type == 'accessories':
            context['accessories'].append(favorite.specialist.accessories)
        elif favorite.specialist.type == 'stylist':
            context['stylists'].append(favorite.specialist.stylist)
        elif favorite.specialist.type == 'photostudio':
            context['photostudios'].append(favorite.specialist.photostudio)
        elif favorite.specialist.type == 'dance':
            context['dance'].append(favorite.specialist.dance)
        elif favorite.specialist.type == 'agency':
            context['agencies'].append(favorite.specialist.agency)
        elif favorite.specialist.type == 'videographer':
            context['videographers'].append(favorite.specialist.videographer)

        
    print(context)

    return render(request, 'account/favorites.html', context)

