from time import timezone
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f'Портфолио {self.user}'

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'


class Image(models.Model):
    image = models.ImageField(upload_to='portfolio/images')
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Review(models.Model):
    service_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_reviews')
    client_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField('Текст отзыва', default=' ')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Отзыв {self.client_user} на {self.service_user}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-created',)


class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/agencies', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    price = models.FloatField('Начальная цена', null=True)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:agency_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Agency, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебное агенство'
        verbose_name_plural = 'Свадебные агенства'
        ordering = ['-is_pro', '-created',]


class Dance(models.Model):
    _TYPE = [
        ('business', 'Компания'),
        ('private', 'Индивидуальные услуги')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена ', null=True)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/dances', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    type = models.CharField(max_length=50, choices=_TYPE, null=True)    
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:dance_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Dance, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебный танец'
        verbose_name_plural = 'Свадебный танец'
        ordering = ['-is_pro', '-created',]


class PhotoStudio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price_per_hour = models.FloatField('Цена за час', null=True)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/photoStudios', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:photostudio_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(PhotoStudio, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотостудия'
        verbose_name_plural = 'Фотостудии'
        ordering = ['-is_pro', '-created',]


class Stylist(models.Model):
    _TYPE = [
        ('business', 'Компания'),
        ('private', 'Индивидуальные услуги')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена ', null=True)
    on_departure = models.BooleanField('На выезд', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/stylists', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.CharField(max_length=50, choices=_TYPE, null=True)    
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:stylist_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Stylist, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Стилист, визажист'
        verbose_name_plural = 'Стилисты, визажисты'
        ordering = ['-is_pro', '-created',]


class Accessories(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    rent = models.BooleanField('На прокат', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/accessories', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.FloatField('Цена', null=True)
    accessories_type = models.ManyToManyField('AccessoriesType', null=True)    
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:accessories_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Accessories, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебные аксессуары'
        verbose_name_plural = 'Свадебные аксессуары'
        ordering = ['-is_pro', '-created',]


class AccessoriesType(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self)   :
        return self.name

    class Meta:
        verbose_name = 'Тип аксессуаров'
        verbose_name_plural = 'Типы аксессуаров'


class Costume(models.Model):
    _CONDITION_TYPES = [
        ('sale', 'Продажа'),
        ('rent', 'Аренд')
    ]
    _TYPE = [
        ('business', 'Компания'),
        ('private', 'Индивидуальные услуги')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    type = models.CharField(max_length=50, choices=_TYPE, null=True)    
    condition = models.CharField(max_length=50, choices=_CONDITION_TYPES, null=True, verbose_name='Вид сделки')
    price = models.FloatField('Начальная цена', null=True)
    rent = models.BooleanField('На прокат', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/costumes', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:costume_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Costume, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебный костюм'
        verbose_name_plural = 'Свадебные костюмы'
        ordering = ['-is_pro', '-created',]


class Decor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Минимальная цена украшения зала', null=True)
    avatar = models.ImageField(upload_to='avatars/decors', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:decor_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Decor, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Оформление и декор'
        verbose_name_plural = 'Оформление и декор'
        ordering = ['-is_pro', '-created',]


class Bouquet(models.Model):
    _TYPE = [
        ('business', 'Компания'),
        ('private', 'Индивидуальные услуги')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена', null=True)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/bouquets', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.CharField(max_length=50, choices=_TYPE, null=True)    
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:bouquet_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Bouquet, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебный букет'
        verbose_name_plural = 'Свадебные букеты'
        ordering = ['-is_pro', '-created',]


class Ring(models.Model):
    _TYPE = [
        ('business', 'Компания'),
        ('private', 'Индивидуальные услуги')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/rings', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.FloatField('Цена', null=True)
    type = models.CharField(max_length=50, choices=_TYPE, null=True)    
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:ring_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Ring, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебное кольцо'
        verbose_name_plural = 'Свадебные кольца'
        ordering = ['-is_pro', '-created',]


class Dress(models.Model):
    _DRESS_TYPES = [
        ('bouffant', 'Пышное'),
        ('straight', 'Прямое')
    ]
    _CONDITION_TYPES = [
        ('sale', 'Продажа'),
        ('rent', 'Аренд')
    ]
    _TYPE = [
        ('business', 'Компания'),
        ('private', 'Индивидуальные услуги')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    type = models.CharField(max_length=50, choices=_TYPE, null=True)
    dress_type = models.CharField(max_length=50, choices=_DRESS_TYPES, null=True, verbose_name='Тип платье')
    condition = models.CharField(max_length=50, choices=_CONDITION_TYPES, null=True, verbose_name='Вид сделки')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/dresses', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    price = models.FloatField('Начальная цена', null=True)
    slug = models.SlugField(max_length=200, unique=True)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:dress_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Dress, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебное платье'
        verbose_name_plural = 'Свадебные платья'
        ordering = ['-is_pro', '-created',]


class Cake(models.Model):
    _TYPES = [
        ('business', 'Компания'),
        ('private', 'Индивидуальные услуги')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    type = models.CharField(max_length=50, choices=_TYPES, null=True)
    price_per_kg = models.FloatField('Цена за кг', null=True)
    price = models.FloatField('Начальная цена', null=True)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/cakes', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:cake_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Cake, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебный торт'
        verbose_name_plural = 'Свадебные торты'
        ordering = ['-is_pro', '-created',]


class Invitation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/invitations', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    price = models.FloatField('Начальная цена', null=True)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:invitation_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Invitation, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пригласительное'
        verbose_name_plural = 'Пригласительные'
        ordering = ['-is_pro', '-created',]


class RegistryOffice(models.Model):
    _REGISTRY_TYPE = [
        ('visiting', 'Выездная'),
        ('not_visiting', 'Не выездная')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/registryOffices', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.CharField(max_length=50, choices=_REGISTRY_TYPE, null=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:registryoffice_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(RegistryOffice, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Дворец бракосочетания, ЗАГС'
        verbose_name_plural = 'Дворцы бракосочтания, ЗАГСы'
        ordering = ['-is_pro', '-created',]


class Presenter(models.Model):
    _COMPOSITION_TYPE = [
        ('duet', 'Дуэт'),
        ('solo', 'Соло'),
    ]
    _GENDER = [
        ('men', 'Мужчина'),
        ('women', 'Женщина'),
        ('mixed', 'Смешанный'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена', null=True)
    price_per_hour = models.FloatField('Цена за час', null=True)
    composition = models.CharField('Состав', max_length=50, choices=_COMPOSITION_TYPE, null=True)
    gender = models.CharField('Пол', max_length=50, choices=_GENDER, null=True)
    language = models.ManyToManyField('Language', verbose_name='Языки')
    avatar = models.ImageField(upload_to='avatars/presenters', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:presenter_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Presenter, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ведущий и тамада'
        verbose_name_plural = 'Ведущие и тамада'
        ordering = ['-is_pro', '-created',]


class Language(models.Model):
    name = models.CharField(("Язык"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Music(models.Model):
    _COMPOSITION_TYPE = [
        ('duet', 'Дуэт'),
        ('solo', 'Соло'),
        ('group', 'Группа'),
        ('dj', 'Dj'),
    ]

    _VOCAL_TYPE = [
        ('men', 'Мужской'),
        ('women', 'Женский'),
        ('mixed', 'Смешанный'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена за выступление', null=True)
    price_per_evening = models.FloatField('Цена за вечер', null=True)
    avatar = models.ImageField(upload_to='avatars/musician', verbose_name='Аватар', blank=True)
    composition = models.CharField('Исполнители', max_length=50, choices=_COMPOSITION_TYPE, null=True)
    vocal = models.CharField('Вокал', max_length=50, choices=_VOCAL_TYPE, null=True)
    language = models.ManyToManyField('Language', verbose_name='Языки исполнения песен')
    phone = models.CharField('Телефон', max_length=13)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:music_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Music, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Музыкальная группа и DJ'
        verbose_name_plural = 'Музыкальные группы и DJ'
        ordering = ['-is_pro', '-created',]


class Transport(models.Model):
    _TRANSPORT_TYPE = [
        ('business', 'Компания'),
        ('private', 'Индивидуальные услуги')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    type = models.CharField(max_length=50, choices=_TRANSPORT_TYPE, null=True)
    price = models.FloatField('Цена', null=True)
    price_per_hour = models.FloatField('Цена за час', null=True)
    with_driver = models.BooleanField('С водителем', default=True)
    avatar = models.ImageField(upload_to='avatars/transports', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)
    car_type = models.ManyToManyField('CarType', verbose_name='Тип автомобиля')
    car_brand = models.ManyToManyField('CarBrand', verbose_name='Марка автомобиля')
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:transport_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Transport, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'
        ordering = ['-is_pro', '-created',]
    

class CarType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип автомобиля'
        verbose_name_plural = 'Типы автомобилей'


class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена', null=True)
    avatar = models.ImageField(upload_to='avatars/artists', verbose_name='Аватар', blank=True)
    type = models.ManyToManyField('ShowType', verbose_name='Тип шоупрограммы', null=True)
    phone = models.CharField('Телефон', max_length=13)
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:artist_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Artist, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Шоу программа, артист'
        verbose_name_plural = 'Шоу программы, артисты'
        ordering = ['-is_pro', '-created',]


class ShowType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип шоупрограммы'
        verbose_name_plural = 'Типы шоупрограмм'


class Restaurant(models.Model):
    # TODO Kitchen type
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название заведения', max_length=155)
    description = models.TextField('Описание')
    average_check = models.FloatField('Средний чек')
    capacity = models.IntegerField('Вместимость')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/restaurants', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.ForeignKey('RestaurantType', on_delete=models.CASCADE, verbose_name='Тип заведения', null=True)
    kitchen = models.ManyToManyField('KitchenType', verbose_name='Кухня')
    additional_services = models.ManyToManyField('RestaurantAdditionalFeeService', verbose_name='Услуги за доп плату')
    benefits = models.ManyToManyField('RestaurantBenefits', verbose_name='Преимущества')
    payment = models.ManyToManyField('RestaurantPaymentMethod', verbose_name='Способы оплаты')
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:restaurant_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Restaurant, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Банкетный зал, ретсоран'
        verbose_name_plural = 'Банкетные залы, рестораны'
        ordering = ['-is_pro', '-created',]


class RestaurantAdditionalFeeService(models.Model):
    name = models.CharField('Название услуги', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Услуга за доп плату'
        verbose_name_plural = 'Услуги за доп плату'


class RestaurantBenefits(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преимущество заведения'
        verbose_name_plural = 'Преимущества заведения'


class RestaurantPaymentMethod(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'


class RestaurantType(models.Model):
    name = models.CharField('Тип заведения', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип заведения'
        verbose_name_plural = 'Типы заведений'


class KitchenType(models.Model):
    name = models.CharField('Название кухни', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кухня'
        verbose_name_plural = 'Кухни'


class Photographer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    full_name = models.CharField('Имя и Фамилия', max_length=155)
    about = models.TextField('О себе')
    price = models.FloatField('Цена', null=True)
    price_per_hour = models.FloatField('Цена за час', null=True)
    avatar = models.ImageField(upload_to='avatars/photographers', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    telegram = models.CharField('Телеграм', max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_average_rating(self):
        return self.user.ratings.ratings_for_instance(self.user).average

    def get_absolute_url(self):
        return reverse('services:photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотограф'
        verbose_name_plural = 'Фотографы'
        ordering = ['-is_pro', '-created',]

