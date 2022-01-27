from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BrideGuest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Телефон', max_length=13)

    class Meta:
        verbose_name = 'Список гостей невесты'


class GroomGuest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Имя', max_length=255)
    phone = models.CharField('Телефон', max_length=13)

    class Meta:
        verbose_name = 'Список гостей жениха'
