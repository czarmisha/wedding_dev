from .models import ClientProfile, Category, City, District, BlockList
from django.contrib import admin
from django.utils.text import slugify
from django.contrib.auth import get_user_model, admin as auth_admin

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


# @admin.register(SpecialistProfile)
# class SpecialistAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         username = obj.user.username
#         obj.slug = slugify(username)
#         obj.user.type = 'specialist'
#         obj.save()


admin.site.register(ClientProfile)
# admin.site.register(Category)
admin.site.register(City)
admin.site.register(District)
admin.site.register(BlockList)
