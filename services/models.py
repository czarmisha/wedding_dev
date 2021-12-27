from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:agency_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Agency, self).save(*args, **kwargs)


class Dance(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена ')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:dance_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Dance, self).save(*args, **kwargs)


class PhotoStudio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена ')
    price_per_hour = models.FloatField('Цена за час')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:photostudio_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(PhotoStudio, self).save(*args, **kwargs)


class Stylist(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена ')
    on_departure = models.BooleanField('На выезд', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:stylist_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Stylist, self).save(*args, **kwargs)


class Accessories(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    rent = models.BooleanField('На прокат', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:accessories_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Accessories, self).save(*args, **kwargs)


class Costume(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    rent = models.BooleanField('На прокат', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:costume_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Costume, self).save(*args, **kwargs)


class Decor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:decor_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Decor, self).save(*args, **kwargs)


class Bouquet(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:bouquet_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Bouquet, self).save(*args, **kwargs)


class Ring(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:ring_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Ring, self).save(*args, **kwargs)


class Dress(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:dress_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Dress, self).save(*args, **kwargs)


class Cake(models.Model):
    #TODO кондитерка ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price_per_kg = models.FloatField('Цена за кг')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:cake_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Cake, self).save(*args, **kwargs)


class Invitation(models.Model):
    #TODO полиграия ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:invitation_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Invitation, self).save(*args, **kwargs)


class RegistryOffice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    on_departure = models.BooleanField('На выезд', default=False)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:registryoffice_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(RegistryOffice, self).save(*args, **kwargs)


class Presenter(models.Model):
    # TODO Language
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:presenter_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Presenter, self).save(*args, **kwargs)


class Music(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    price_per_hour = models.FloatField('Цена за час')
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:music_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Music, self).save(*args, **kwargs)


class Transport(models.Model):
    #TODO индивидуал сёрвис ор компани/ car type
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    price_per_hour = models.FloatField('Цена за час')
    # car_type =
    with_driver = models.BooleanField('С водителем', default=True)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:transport_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Transport, self).save(*args, **kwargs)


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:artist_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Artist, self).save(*args, **kwargs)


class Restaurant(models.Model):
    # TODO Kitchen type
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название заведения', max_length=155)
    description = models.TextField('Описание')
    average_check = models.FloatField('Средний чек')
    capacity = models.IntegerField('Вместимость')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар', blank=True)
    phone = models.IntegerField('Телефон')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:retaurant_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Restaurant, self).save(*args, **kwargs)


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
        return reverse('services:photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


class Service(models.Model):
    name = models.CharField('Название услуги', max_length=155)
