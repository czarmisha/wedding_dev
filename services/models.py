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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
        return reverse('account.photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)


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
