from django.contrib import admin
from .models import *
from django.utils.text import slugify


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'agency'
        obj.user.save()
        obj.save()


@admin.register(Dance)
class DanceAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'dance'
        obj.user.save()
        obj.save()


@admin.register(PhotoStudio)
class PhotoStudioAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'photostudio'
        obj.user.save()
        obj.save()


@admin.register(Stylist)
class StylistAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'stylist'
        obj.user.save()
        obj.save()


@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'accessories'
        obj.user.save()
        obj.save()


@admin.register(Costume)
class CostumeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'costume'
        obj.user.save()
        obj.save()


@admin.register(Decor)
class DecorAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'decor'
        obj.user.save()
        obj.save()


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'bouquet'
        obj.user.save()
        obj.save()


@admin.register(Ring)
class RingAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'ring'
        obj.user.save()
        obj.save()


@admin.register(Dress)
class DressAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'dress'
        obj.user.save()
        obj.save()


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'cake'
        obj.user.save()
        obj.save()


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'invitation'
        obj.user.save()
        obj.save()


@admin.register(RegistryOffice)
class RegistryOfficeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'registryoffice'
        obj.user.save()
        obj.save()


@admin.register(Presenter)
class PresenterAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'presenter'
        obj.user.save()
        obj.save()


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'music'
        obj.user.save()
        obj.save()


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'transport'
        obj.user.save()
        obj.save()


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'artist'
        obj.user.save()
        obj.save()


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'restaurant'
        obj.user.save()
        obj.save()


@admin.register(Photographer)
class PhotographerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'photographer'
        obj.user.save()
        obj.save()


@admin.register(Videographer)
class VideographerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'videographer'
        obj.user.save()
        obj.save()


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(RestaurantType)
class RestaurantTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(KitchenType)
class KitchenTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(RestaurantAdditionalFeeService)
class RestaurantAdditionalFeeServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(RestaurantBenefits)
class RestaurantBenefitsAdmin(admin.ModelAdmin):
    pass


@admin.register(RestaurantPaymentMethod)
class RestaurantPaymentMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(ShowType)
class ShowTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(AccessoriesType)
class AccessoriesTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    pass

