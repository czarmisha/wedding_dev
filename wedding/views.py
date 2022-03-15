import telebot
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
        spec_name = request.POST.get('name')
        spec_phone = request.POST.get('phone')
        bot_token = '5164361466:AAFFuHU1szO-4MQKjcKK5aVM_TBCDxJVqzg'
        chat_id = '-703685470'
        txt = f'Новый специиалист хочет зарегистрироваться \n\n <b>Имя</b>: {spec_name} \n <b>Телефон</b>: {spec_phone}'
        bot = telebot.TeleBot(bot_token)
        try:
            bot.send_message(
            chat_id=chat_id,
            text=txt,
            parse_mode='HTML'
        )
        except:
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
    