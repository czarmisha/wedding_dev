from .models import ClientProfile, SpecialistProfile, Category, City, District
from django.contrib import admin
from django.utils.text import slugify
from django.contrib.auth import get_user_model, admin as auth_admin

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    pass


@admin.register(SpecialistProfile)
class SpecialistAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        username = obj.user.username
        #if form.cleaned_data['slug'] == "":
        obj.slug = slugify(username)
        obj.save()


admin.site.register(ClientProfile)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(District)
