from django.contrib import admin
from .models import Tender
from django.contrib.auth import admin as auth_admin


# @admin.register(Tender)
# class TenderAdmin(auth_admin.UserAdmin):
#     pass


admin.site.register(Tender)
