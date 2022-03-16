from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Tender(models.Model):
    _SERVICES = [
        ('photographer', _('Фотограф')),
        ('artist', _('Артист, Шоу программа')),
        ('transport', _('Транспорт')),
        ('music', _('Музыканты, Dj')),
        ('presenter', _('Ведущий')),
        ('invitation', _('Пригласительные')),
        ('cake', _('Торт')),
        ('dress', _('Платье')),
        ('ring', _('Кольца')),
        ('bouquet', _('Букет')),
        ('decor', _('Декор, оформление')),
        ('costume', _('Костюм')),
        ('accessories', _('Аксессуары')),
        ('stylist', _('Стилист, Визажист')),
        ('photostudio', _('Фотостудия')),
        ('dance', _('Танец')),
        ('agency', _('Агенство')),
        ('videographer', _('Видеограф')),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='executor', blank=True)
    # response = models.ManyToManyField(User, related_name='responses', blank=True)
    service = models.CharField(_('Услуга'), max_length=15, choices=_SERVICES, default=None)
    create_date = models.DateTimeField(_('Дата создания тендера'), auto_now_add=True)
    on_date = models.DateField(_('Дата события'))
    budget = models.FloatField(_('Бюджет (y.e.)'))
    comment = models.TextField(_('Комментарий'), blank=True)
    slug = models.SlugField(max_length=200, unique=True, default='sometender', blank=True)

    def __str__(self):
        return f'Тендер {self.author} на поиск {self.service}'

    def get_absolute_url(self):
        return reverse('tender:detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author.username + self.service + str(self.on_date))
        super(Tender, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тендер'
        verbose_name_plural = 'Тендеры'
        ordering = ['-create_date']


class Response(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE, related_name='responses')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responses')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Отклик {self.from_user} на {self.tender}'

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
        ordering = ['-created']
