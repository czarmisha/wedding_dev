from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import BrideGuest, GroomGuest

User = get_user_model()


@login_required
def guest_list_view(request):
    try:
        bride_list = BrideGuest.objects.filter(user=request.user)
        groom_list = GroomGuest.objects.filter(user=request.user)
    except:
        bride_list = None
        groom_list = None
    return render(request, template_name='guest_list/guest_list.html', context={'bride_list': bride_list,
                                                                                'groom_list': groom_list,
                                                                                })


@login_required
def guest_save(request):
    if request.method == 'POST':
        success = False
        err = ''
        if request.user.type == 'client':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            if request.POST.get('type') == 'bride':
                try:
                    guest = BrideGuest(user=request.user, name=name, phone=phone)
                except:
                    guest = None
            else:
                try:
                    guest = GroomGuest(user=request.user, name=name, phone=phone)
                except:
                    guest = None

            guest.save()
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
def guest_delete(request):
    if request.method == 'POST':
        success = False
        err = ''
        if request.user.type == 'client':
            pk = request.POST.get('obj_pk')
            if request.POST.get('type') == 'bride':
                guest = BrideGuest.objects.filter(user=request.user, pk=pk).first()
                if guest:
                    guest.delete()
            else:
                guest = GroomGuest.objects.filter(user=request.user, pk=pk).first()
                if guest:
                    guest.delete()

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
