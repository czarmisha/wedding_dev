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
        'trasport': [],
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
        'count': favorites_count
    }

    for favorite in all_favorites_for_client:
        if favorite.specialist.type == 'photographer':
            context['photographers'].append(favorite.specialist.photographer)
        elif favorite.specialist.type == 'restaurant':
            context['restaurants'].append(favorite.specialist.restaurant)
        
        print(context)

    return render(request, 'account/favorites.html', context)

