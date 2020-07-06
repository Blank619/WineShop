from django.contrib import admin
from django import forms
# Register your models here.
from .models import RegisterItem,Cart,cust_details
from django.contrib.auth.admin import UserAdmin



admin.site.register(RegisterItem)
admin.site.register(Cart)
admin.site.register(cust_details)

#admin.site.register(CustomFields)
#admin.site.unregister(User)
