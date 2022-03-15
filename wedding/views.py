from django.shortcuts import render
from tender.models import Tender
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def home(request):
    tenders = Tender.objects.all()[:3]
    tender_count = Tender.objects.all().count()
    return render(request, 'wedding/home.html', context={'tenders': tenders, 'tender_count': tender_count})

def promo(request):
    if request.method == 'POST':
        spec_name = request.POST.get('service_user_pk')
        spec_phone = request.POST.get('client_user_pk')
        messages.error(request, 'Форма не отправлена. Попробуйте позже.')
        return render(request, 'wedding/promo.html', context={
            'form': False,
            'text': _('Форма отправлена, спасибо! Администратор свяжется с Вами в ближайшее время'),
            })
    else:
        return render(request, 'wedding/promo.html', context={'form': True})

def catalog(request):
    return render(request, 'services/catalog.html', context={})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
    