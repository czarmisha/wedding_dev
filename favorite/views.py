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

