from django.contrib import admin
from django import forms
# Register your models here.
from .models import RegisterItem
from django.contrib.auth.admin import UserAdmin



admin.site.register(RegisterItem)

#admin.site.register(CustomFields)
#admin.site.unregister(User)
