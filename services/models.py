from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

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

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        # ordering = ('bar_date', 'related.name',)


class Agency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/agencies', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Dance(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена ')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/dances', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class PhotoStudio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена ')
    price_per_hour = models.FloatField('Цена за час')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/photoStudios', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Stylist(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена ')
    on_departure = models.BooleanField('На выезд', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/stylists', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Accessories(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    rent = models.BooleanField('На прокат', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/accessories', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Costume(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    rent = models.BooleanField('На прокат', default=False)
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/costumes', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Decor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    avatar = models.ImageField(upload_to='avatars/decors', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Bouquet(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/bouquets', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Ring(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/rings', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Dress(models.Model):
    #TODO свадебный слаон ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/dresses', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Cake(models.Model):
    #TODO кондитерка ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price_per_kg = models.FloatField('Цена за кг')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/cakes', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Invitation(models.Model):
    #TODO полиграия ил индвид
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    avatar = models.ImageField(upload_to='avatars/invitations', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class RegistryOffice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=500)
    on_departure = models.BooleanField('На выезд', default=False)
    avatar = models.ImageField(upload_to='avatars/registryOffices', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Presenter(models.Model):
    # TODO Language
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    avatar = models.ImageField(upload_to='avatars/presenters', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:presenter_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Presenter, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ведущий'
        verbose_name_plural = 'Ведущие'


class Music(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    price_per_hour = models.FloatField('Цена за час')
    avatar = models.ImageField(upload_to='avatars/musician', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:music_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Music, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Музыкальная группа, DJ'
        verbose_name_plural = 'Музыкальные группы, DJ'


class Transport(models.Model):
    #TODO индивидуал сёрвис ор компани/ car type
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    price_per_hour = models.FloatField('Цена за час')
    # car_type =
    with_driver = models.BooleanField('С водителем', default=True)
    avatar = models.ImageField(upload_to='avatars/transports', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название ', max_length=155)
    description = models.TextField('Описание')
    price = models.FloatField('Цена')
    avatar = models.ImageField(upload_to='avatars/artists', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    slug = models.SlugField(max_length=200, unique=True)

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

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:retaurant_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Restaurant, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Банкетный зал, ретсоран'
        verbose_name_plural = 'Банкетные залы, рестораны'


class Photographer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    full_name = models.CharField('Имя и Фамилия', max_length=155)
    about = models.TextField('О себе')
    price = models.FloatField('Цена')
    price_per_hour = models.FloatField('Цена за час')
    avatar = models.ImageField(upload_to='avatars/photographers', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    telegram = models.CharField('Телеграм', max_length=50)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('services:photographer_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Photographer, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фотограф'
        verbose_name_plural = 'Фотографы'

