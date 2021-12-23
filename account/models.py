from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify


class User(AbstractUser):
    _TYPES_OF_USER = (
        ('client', 'Клиент'),
        ('specialist', 'Специалист'),
        ('other', 'Другой'),
    )
    type = models.CharField('Тип пользователя', max_length=10, choices=_TYPES_OF_USER, default='client')


class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"pk": self.pk})


class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название города')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название района')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город района')

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return self.name


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар')
    phone = models.IntegerField('Телефон')
    telegram = models.CharField('Телеграм', max_length=50)
    create_date = models.DateTimeField('Дата создания профиля', auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, default='defaultclient')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(ClientProfile, self).save(*args, **kwargs)


class SpecialistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='specialists')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар')
    phone = models.IntegerField('Телефон')
    telegram = models.CharField('Телеграм', max_length=50)
    create_date = models.DateTimeField('Дата создания профиля', auto_now_add=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    district = models.ForeignKey('District', on_delete=models.CASCADE, verbose_name='Район', blank=True, null=True)
    about = models.TextField('О себе', max_length=10000)

    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('account.specialist_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(SpecialistProfile, self).save(*args, **kwargs)