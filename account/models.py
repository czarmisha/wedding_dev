from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
# from tender.models import Tender


class User(AbstractUser):
    type = models.CharField(
        'Тип пользователя', max_length=155, default='client')
    rating = models.FloatField('Рейтинг пользователя', default=0)

    # def __str__(self):
    #     return self.username

    def get_calculated_rate(self):
        return int(self.get_positive_rate_count())*1 + int(self.get_neutral_rate_count())*.5 - int(self.get_negative_rate_count())*1

    def get_reviews_count(self):
        return self.service_reviews.count()

    def get_negative_rate_count(self):
        return self.service_reviews.filter(value=1).count()

    def get_neutral_rate_count(self):
        return self.service_reviews.filter(value=2).count()

    def get_positive_rate_count(self):
        return self.service_reviews.filter(value=3).count()

    def __str__(self):
        if self.type == 'client':
            return self.first_name + " " + self.last_name
        elif self.type == 'photographer':
            return self.photographer.name
        elif self.type == 'restaurant':
            return self.restaurant.name
        elif self.type == 'artist':
            return self.artist.name
        elif self.type == 'transport':
            return self.transport.name
        elif self.type == 'music':
            return self.music.name
        elif self.type == 'presenter':
            return self.presenter.name
        elif self.type == 'registryoffice':
            return self.registryoffice.name
        elif self.type == 'invitation':
            return self.invitation.name
        elif self.type == 'cake':
            return self.cake.name
        elif self.type == 'dress':
            return self.dress.name
        elif self.type == 'ring':
            return self.ring.name
        elif self.type == 'bouquet':
            return self.bouquet.name
        elif self.type == 'decor':
            return self.decor.name
        elif self.type == 'costume':
            return self.costume.name
        elif self.type == 'accessories':
            return self.accessories.name
        elif self.type == 'stylist':
            return self.stylist.name
        elif self.type == 'photostudio':
            return self.photostudio.name
        elif self.type == 'dance':
            return self.dance.name
        elif self.type == 'agency':
            return self.agency.name
        elif self.type == 'videographer':
            return self.videographer.name


    def check_avatar(self):
        if self.type == 'client':
            return self.clientprofile.avatar
        elif self.type == 'photographer':
            return self.photographer.avatar
        elif self.type == 'restaurant':
            return self.restaurant.avatar
        elif self.type == 'artist':
            return self.artist.avatar
        elif self.type == 'transport':
            return self.transport.avatar
        elif self.type == 'music':
            return self.music.avatar
        elif self.type == 'presenter':
            return self.presenter.avatar
        elif self.type == 'registryoffice':
            return self.registryoffice.avatar
        elif self.type == 'invitation':
            return self.invitation.avatar
        elif self.type == 'cake':
            return self.cake.avatar
        elif self.type == 'dress':
            return self.dress.avatar
        elif self.type == 'ring':
            return self.ring.avatar
        elif self.type == 'bouquet':
            return self.bouquet.avatar
        elif self.type == 'decor':
            return self.decor.avatar
        elif self.type == 'costume':
            return self.costume.avatar
        elif self.type == 'accessories':
            return self.accessories.avatar
        elif self.type == 'stylist':
            return self.stylist.avatar
        elif self.type == 'photostudio':
            return self.photostudio.avatar
        elif self.type == 'dance':
            return self.dance.avatar
        elif self.type == 'agency':
            return self.agency.avatar
        elif self.type == 'videographer':
            return self.videographer.avatar

    def get_cabinet_url(self):
        if self.type == 'client':
            return reverse('account:cabinet', args=[self.pk])
        elif self.type == 'photographer':
            return reverse('services:photographer_detail', args=[self.photographer.slug])
        elif self.type == 'restaurant':
            return reverse('services:restaurant_detail', args=[self.restaurant.slug])
        elif self.type == 'artist':
            return reverse('services:artist_detail', args=[self.artist.slug])
        elif self.type == 'transport':
            return reverse('services:transport_detail', args=[self.transport.slug])
        elif self.type == 'music':
            return reverse('services:music_detail', args=[self.music.slug])
        elif self.type == 'presenter':
            return reverse('services:presenter_detail', args=[self.presenter.slug])
        elif self.type == 'registryoffice':
            return reverse('services:registryoffice_detail', args=[self.registryoffice.slug])
        elif self.type == 'invitation':
            return reverse('services:invitation_detail', args=[self.invitation.slug])
        elif self.type == 'cake':
            return reverse('services:cake_detail', args=[self.cake.slug])
        elif self.type == 'dress':
            return reverse('services:dress_detail', args=[self.dress.slug])
        elif self.type == 'ring':
            return reverse('services:ring_detail', args=[self.ring.slug])
        elif self.type == 'bouquet':
            return reverse('services:bouquet_detail', args=[self.bouquet.slug])
        elif self.type == 'decor':
            return reverse('services:decor_detail', args=[self.decor.slug])
        elif self.type == 'costume':
            return reverse('services:costume_detail', args=[self.costume.slug])
        elif self.type == 'accessories':
            return reverse('services:accessories_detail', args=[self.accessories.slug])
        elif self.type == 'stylist':
            return reverse('services:stylist_detail', args=[self.stylist.slug])
        elif self.type == 'photostudio':
            return reverse('services:photostudio_detail', args=[self.photostudio.slug])
        elif self.type == 'dance':
            return reverse('services:dance_detail', args=[self.dance.slug])
        elif self.type == 'agency':
            return reverse('services:agency_detail', args=[self.agency.slug])
        elif self.type == 'videographer':
            return reverse('services:videographer_detail', args=[self.videographer.slug])


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
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, verbose_name='Город района')

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return self.name


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    avatar = models.ImageField(
        upload_to='avatars/clients', verbose_name='Аватар', blank=True)
    phone = models.CharField('Телефон', max_length=13)
    telegram = models.CharField('Телеграм', max_length=50)
    create_date = models.DateTimeField(
        'Дата создания профиля', auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True,
                            default='defaultclient')

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('account:cabinet', args=[self.user.pk])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(ClientProfile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


# class SpecialistProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
#     category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория',
#                                  related_name='specialists')
#     avatar = models.ImageField(upload_to='avatars/specialists', verbose_name='Аватар')
#     phone = models.IntegerField('Телефон')
#     telegram = models.CharField('Телеграм', max_length=50)
#     create_date = models.DateTimeField('Дата создания профиля', auto_now_add=True)
#     city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
#     district = models.ForeignKey('District', on_delete=models.CASCADE, verbose_name='Район', blank=True, null=True)
#     about = models.TextField('О себе', max_length=10000)
#
#     slug = models.SlugField(max_length=200, unique=True)
#
#     def __str__(self):
#         return self.user.username
#
#     def get_absolute_url(self):
#         return reverse('account.specialist_detail', args=[str(self.slug)])
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.user.username)
#         super(SpecialistProfile, self).save(*args, **kwargs)


# class FavoriteBase(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.user.username
#
#
# class FavoriteService(FavoriteBase):
#     obj = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class FavoriteTender(FavoriteBase):
#     obj = models.ForeignKey(Tender, on_delete=models.CASCADE)
