from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class Tender(models.Model):
    _SERVICES = [
        ('photographer', 'Фотограф'),
        ('artist', 'Артист, Шоу программа'),
        ('transport', 'Транспорт'),
        ('music', 'Музыканты, Dj'),
        ('presenter', 'Ведущий'),
        ('invitation', 'Пригласительные'),
        ('cake', 'Торт'),
        ('dress', 'Платье'),
        ('ring', 'Кольца'),
        ('bouquet', 'Букет'),
        ('decor', 'Декор, оформление'),
        ('costume', 'Костюм'),
        ('accessories', 'Аксуссуары'),
        ('stylist', 'Стилист, Визажист'),
        ('photostudio', 'Фотостудия'),
        ('dance', 'Танец'),
        ('agency', 'Агенство'),
        ('videographer', 'Видеограф'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='executor', blank=True)
    # response = models.ManyToManyField(User, related_name='responses', blank=True)
    service = models.CharField(max_length=15, choices=_SERVICES, default=None)
    create_date = models.DateTimeField('Дата создания тендера', auto_now_add=True)
    on_date = models.DateField('Дата события')
    budget = models.FloatField('Бюджет')
    comment = models.TextField('Комментарий', blank=True)
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
