from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


class Photographer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    full_name = models.CharField('Имя и Фамилия', max_length=155)
    about = models.TextField('О себе')
    price = models.FloatField('Цена')
    price_per_hour = models.FloatField('Цена за час')
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    telegram = models.CharField('Телеграм', max_length=50)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


class Service(models.Model):
    name = models.CharField('Название услуги', max_length=155)
