from django.contrib import admin
from .models import Photographer
from django.utils.text import slugify


@admin.register(Photographer)
class PhotographerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        obj.slug = slugify(username)
        obj.user.type = 'photographer'
        obj.user.save()
        obj.save()
