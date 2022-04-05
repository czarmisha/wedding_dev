from django.contrib import admin
from .models import Tender, Response
from django.contrib.auth import admin as auth_admin


# @admin.register(Tender)
# class TenderAdmin(auth_admin.UserAdmin):
#     pass


admin.site.register(Tender)
admin.site.register(Response)

