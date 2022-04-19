from time import timezone
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

User = get_user_model()


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return f'Портфолио {self.user}'

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'


def user_directory_path(instance, filename):
    return f'portfolio/{instance.portfolio.user.username}/{filename}'


class File(models.Model):
    file = models.FileField(upload_to=user_directory_path, default='portfolio/images')
    content_type = models.CharField(max_length=155)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='files')

    class Meta:
        verbose_name = 'Фото/видео'
        verbose_name_plural = 'Фото/видео'


class Video(models.Model):
    videofile = models.FileField(upload_to='portfolio/videos/%Y/%m/%d/', null=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='videos')
    uploaded   = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Review(models.Model):
    service_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_reviews')
    client_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField('Текст отзыва', default=' ')
    value = models.IntegerField('Значение оценки', default=0) # 0-not rated, 1-negative, 2-neutral, 3-positive
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
    description = RichTextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/agencies', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Agency, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебное агенство'
        verbose_name_plural = 'Свадебные агенства'
        ordering = ['-is_pro', '-created',]


class Dance(models.Model):
    _TYPE = [
        ('business', _('Компания')),
        ('private', _('Индивидуальные услуги'))
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    price = models.IntegerField('Цена ', null=True)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/dances', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Dance, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебный танец'
        verbose_name_plural = 'Свадебный танец'
        ordering = ['-is_pro', '-created',]


class PhotoStudio(models.Model):
    _TYPE = [
        ('1', _('Фотостудии')),
        ('2', _('Локации для фотосессий'))
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    price_per_hour = models.IntegerField('Цена за час', null=True)
    address = models.CharField('Адрес', max_length=500)
    type = models.CharField(max_length=50, choices=_TYPE, null=True)  
    avatar = models.ImageField(upload_to='avatars/photoStudios', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    location = models.ForeignKey('account.District', on_delete=models.CASCADE, verbose_name='Местоположение', null=True)
    additional_services = models.ManyToManyField('PhotostudioAdditionalFeeService', verbose_name='Услуги за доп плату')
    benefits = models.ManyToManyField('PhotostudioBenefits', verbose_name='Преимущества')
    payment = models.ManyToManyField('PhotostudioPaymentMethod', verbose_name='Способы оплаты')
    telegram = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:photostudio_detail', args=[str(self.slug)])

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(PhotoStudio, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Площадка для фотосессий'
        verbose_name_plural = 'Площадки для фотосессий'
        ordering = ['-is_pro', '-created',]


class PhotostudioAdditionalFeeService(models.Model):
    name = models.CharField('Название услуги', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотостудии - Услуга за доп плату'
        verbose_name_plural = 'Фотостудии - Услуги за доп плату'


class PhotostudioBenefits(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотостудии - Преимущество заведения'
        verbose_name_plural = 'Фотостудии - Преимущества заведения'


class PhotostudioPaymentMethod(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотостудии - Способ оплаты'
        verbose_name_plural = 'Фотостудии - Способы оплаты'


class Stylist(models.Model):
    _TYPE = [
        ('business', _('Компания')),
        ('private', _('Индивидуальные услуги'))
    ]
    _SERVICE_TYPE = [
        ('1', _('Свадебная причёска')),
        ('2', _('Свадебный маникюр')),
        ('3', _('Свадебный макияж'))
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    price = models.IntegerField('Цена ', null=True)
    on_departure = models.BooleanField('На выезд', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/stylists', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    type = models.CharField(max_length=50, choices=_TYPE, null=True)
    service_type = models.CharField(max_length=50, choices=_SERVICE_TYPE, null=True, verbose_name='Вид услуги')
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

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
    description = RichTextField('Описание')
    rent = models.BooleanField('На прокат', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/accessories', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.IntegerField('Цена', null=True)
    accessories_type = models.ManyToManyField('AccessoriesType')    
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

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
        ('sale', _('Продажа')),
        ('rent', _('Арендa'))
    ]
    _TYPE = [
        ('business', _('Компания')),
        ('private', _('Индивидуальные услуги'))
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    type = models.CharField(max_length=50, choices=_TYPE, null=True)    
    condition = models.CharField(max_length=50, choices=_CONDITION_TYPES, null=True, verbose_name='Вид сделки')
    price = models.IntegerField('Начальная цена', null=True)
    # rent = models.BooleanField('На прокат', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/costumes', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

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
    description = RichTextField('Описание')
    price = models.IntegerField('Минимальная цена украшения зала', null=True)
    avatar = models.ImageField(upload_to='avatars/decors', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Decor, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Оформление и декор'
        verbose_name_plural = 'Оформление и декор'
        ordering = ['-is_pro', '-created',]


class Bouquet(models.Model):
    _TYPE = [
        ('business', _('Компания')),
        ('private', _('Индивидуальные услуги'))
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    price = models.IntegerField('Цена', null=True)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/bouquets', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Bouquet, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебный букет'
        verbose_name_plural = 'Свадебные букеты'
        ordering = ['-is_pro', '-created',]


class Ring(models.Model):
    _TYPE = [
        ('business', _('Компании')),
        ('private', _('Индивидуальные услуги'))
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/rings', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.IntegerField('Цена', null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Ring, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебное кольцо'
        verbose_name_plural = 'Свадебные кольца'
        ordering = ['-is_pro', '-created',]


class Dress(models.Model):
    _CONDITION_TYPES = [
        ('sale', _('Продажа')),
        ('rent', _('Арендa'))
    ]
    _TYPE = [
        ('business', _('Компания')),
        ('private', _('Индивидуальные услуги'))
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    type = models.CharField(max_length=50, choices=_TYPE, null=True, verbose_name='Тип услуги')
    condition = models.CharField(max_length=50, choices=_CONDITION_TYPES, null=True, verbose_name='Вид сделки')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/dresses', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
    price = models.IntegerField('Начальная цена', null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Dress, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Свадебное платье'
        verbose_name_plural = 'Свадебные платья'
        ordering = ['-is_pro', '-created',]


class Cake(models.Model):
    _TYPES = [
        ('business', _('Компания')),
        ('private', _('Индивидуальные услуги'))
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    type = models.CharField(max_length=50, choices=_TYPES, null=True)
    price_per_kg = models.IntegerField('Цена за кг', null=True)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/cakes', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

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
    description = RichTextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/invitations', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Invitation, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пригласительное'
        verbose_name_plural = 'Пригласительные'
        ordering = ['-is_pro', '-created',]


class RegistryOffice(models.Model):
    _REGISTRY_TYPE = [
        ('visiting', _('Выездная')),
        ('not_visiting', _('Невыездная'))
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/registryOffices', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(RegistryOffice, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Дворец бракосочетания, ЗАГС'
        verbose_name_plural = 'Дворцы бракосочетания, ЗАГСы'
        ordering = ['-is_pro', '-created',]


class Presenter(models.Model):
    _COMPOSITION_TYPE = [
        ('solo', _('Соло')),
        ('duet', _('Дуэт')),
    ]
    _GENDER = [
        ('men', _('Мужчина')),
        ('women', _('Женщина')),
        ('mixed', _('Смешанный')),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    price = models.IntegerField('Цена', null=True)
    price_per_hour = models.IntegerField('Цена за час', null=True)
    composition = models.CharField('Состав', max_length=50, choices=_COMPOSITION_TYPE, null=True)
    gender = models.CharField('Пол', max_length=50, choices=_GENDER, null=True)
    language = models.ManyToManyField('Language', verbose_name='Языки')
    avatar = models.ImageField(upload_to='avatars/presenters', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
    additional_services = models.ManyToManyField('PresenterAdditionalFeeService', verbose_name='Услуги за доп плату')
    benefits = models.ManyToManyField('PresenterBenefits', verbose_name='Преимущества')
    payment = models.ManyToManyField('PresenterPaymentMethod', verbose_name='Способы оплаты')
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Presenter, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ведущий и тамада'
        verbose_name_plural = 'Ведущие и тамада'
        ordering = ['-is_pro', '-created',]


class PresenterAdditionalFeeService(models.Model):
    name = models.CharField('Название услуги', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ведущие - Услуга за доп плату'
        verbose_name_plural = 'Ведущие - Услуги за доп плату'


class PresenterBenefits(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ведущие - Преимущество заведения'
        verbose_name_plural = 'Ведущие - Преимущества заведения'


class PresenterPaymentMethod(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ведущие - Способ оплаты'
        verbose_name_plural = 'Ведущие - Способы оплаты'


class Language(models.Model):
    name = models.CharField(("Язык"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Music(models.Model):
    _COMPOSITION_TYPE = [
        ('solo', _('Соло')),
        ('duet', _('Дуэт')),
        ('group', _('Группа')),
        ('dj', _('Dj')),
    ]

    _VOCAL_TYPE = [
        ('men', _('Мужской')),
        ('women', _('Женский')),
        ('mixed', _('Смешанный')),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    price = models.IntegerField('Цена за выступление', null=True)
    avatar = models.ImageField(upload_to='avatars/musician', verbose_name='Аватар', blank=True)
    composition = models.CharField('Исполнители', max_length=50, choices=_COMPOSITION_TYPE, null=True)
    vocal = models.CharField('Вокал', max_length=50, choices=_VOCAL_TYPE, null=True)
    language = models.ManyToManyField('Language', verbose_name='Язык исполнения песен')
    additional_services = models.ManyToManyField('MusicAdditionalFeeService', verbose_name='Услуги за доп плату')
    benefits = models.ManyToManyField('MusicBenefits', verbose_name='Преимущества')
    payment = models.ManyToManyField('MusicPaymentMethod', verbose_name='Способы оплаты')
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Music, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Музыкальная группа и DJ'
        verbose_name_plural = 'Музыкальные группы и DJ'
        ordering = ['-is_pro', '-created',]


class MusicAdditionalFeeService(models.Model):
    name = models.CharField('Название услуги', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Музыканты - Услуга за доп плату'
        verbose_name_plural = 'Музыканты - Услуги за доп плату'


class MusicBenefits(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Музыканты - Преимущество заведения'
        verbose_name_plural = 'Музыканты - Преимущества заведения'


class MusicPaymentMethod(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Музыканты - Способ оплаты'
        verbose_name_plural = 'Музыканты - Способы оплаты'


class Transport(models.Model):
    _TYPE = [
        ('business', _('Компания')),
        ('private', _('Индивидуальные услуги'))
    ]
    _WITH_DRIVER_TYPE = [
        ('1', _('С водителем')),
        ('2', _('Без водителя'))
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = RichTextField('Описание')
    type = models.CharField(max_length=50, choices=_TYPE, null=True)
    price = models.IntegerField('Цена', null=True)
    with_driver = models.CharField(max_length=50, choices=_WITH_DRIVER_TYPE, null=True)
    avatar = models.ImageField(upload_to='avatars/transports', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

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
    description = RichTextField('Описание')
    price = models.IntegerField('Цена', null=True)
    avatar = models.ImageField(upload_to='avatars/artists', verbose_name='Аватар', blank=True)
    type = models.ManyToManyField('ShowType', verbose_name='Тип шоупрограммы')
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название заведения', max_length=155)
    description = RichTextField('Описание')
    average_check = models.IntegerField('Средний чек')
    capacity = models.IntegerField('Вместимость')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/restaurants', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
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

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Restaurant, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Банкетный зал, ресторан'
        verbose_name_plural = 'Банкетные залы, рестораны'
        ordering = ['-is_pro', '-created',]


class RestaurantAdditionalFeeService(models.Model):
    name = models.CharField('Название услуги', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ресторан - Услуга за доп плату'
        verbose_name_plural = 'Ресторан - Услуги за доп плату'


class RestaurantBenefits(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ресторан - Преимущество заведения'
        verbose_name_plural = 'Ресторан - Преимущества заведения'


class RestaurantPaymentMethod(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ресторан - Способ оплаты'
        verbose_name_plural = 'Ресторан - Способы оплаты'


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
    name = models.CharField('Имя и Фамилия', max_length=155)
    about = RichTextField('О себе')
    price = models.IntegerField('Цена', null=True)
    price_per_hour = models.IntegerField('Цена за час', null=True)
    avatar = models.ImageField(upload_to='avatars/photographers', verbose_name='Аватар', blank=True)
    additional_services = models.ManyToManyField('PhotographerAdditionalFeeService', verbose_name='Услуги за доп плату')
    benefits = models.ManyToManyField('PhotographerBenefits', verbose_name='Преимущества')
    payment = models.ManyToManyField('PhotographerPaymentMethod', verbose_name='Способы оплаты')
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
    telegram = models.CharField('Телеграм', max_length=50)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:photographer_detail', args=[str(self.slug)])

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотограф'
        verbose_name_plural = 'Фотографы'
        ordering = ['-is_pro', '-created',]


class PhotographerAdditionalFeeService(models.Model):
    name = models.CharField('Название услуги', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотограф - Услуга за доп плату'
        verbose_name_plural = 'Фотограф - Услуги за доп плату'


class PhotographerBenefits(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотограф - Преимущество заведения'
        verbose_name_plural = 'Фотограф - Преимущества заведения'


class PhotographerPaymentMethod(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотограф - Способ оплаты'
        verbose_name_plural = 'Фотограф - Способы оплаты'


class Videographer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Имя и Фамилия', max_length=155)
    about = RichTextField('О себе')
    price = models.IntegerField('Цена', null=True)
    price_per_hour = models.IntegerField('Цена за час', null=True)
    avatar = models.ImageField(upload_to='avatars/videographers', verbose_name='Аватар', blank=True)
    additional_services = models.ManyToManyField('VideographerAdditionalFeeService', verbose_name='Услуги за доп плату')
    benefits = models.ManyToManyField('VideographerBenefits', verbose_name='Преимущества')
    payment = models.ManyToManyField('VideographerPaymentMethod', verbose_name='Способы оплаты')
    phone = models.CharField('Телефон', max_length=13)
    phone2 = models.CharField('Телефон №2', max_length=13, null=True)
    phone3 = models.CharField('Телефон №3', max_length=13, null=True)
    telegram = models.CharField('Телеграм', max_length=50)
    instagram = models.CharField(max_length=155, blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    is_pro = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:videographer_detail', args=[str(self.slug)])

    # def get_average_rating(self):
    #     return self.user.ratings.ratings_for_instance(self.user).average

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Видеограф'
        verbose_name_plural = 'Видеографы'
        ordering = ['-is_pro', '-created',]


class VideographerAdditionalFeeService(models.Model):
    name = models.CharField('Название услуги', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Видеограф - Услуга за доп плату'
        verbose_name_plural = 'Видеограф - Услуги за доп плату'


class VideographerBenefits(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Видеограф - Преимущество заведения'
        verbose_name_plural = 'Видеограф - Преимущества заведения'


class VideographerPaymentMethod(models.Model):
    name = models.CharField('Название', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Видеограф - Способ оплаты'
        verbose_name_plural = 'Видеограф - Способы оплаты'
