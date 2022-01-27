from django.contrib import admin
from .models import BrideGuest, GroomGuest


@admin.register(BrideGuest)
class BrideGuestAdmin(admin.ModelAdmin):
    pass


@admin.register(GroomGuest)
class GroomGuestAdmin(admin.ModelAdmin):
    pass

