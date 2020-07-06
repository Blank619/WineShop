from django.db import models
from django import forms
from django.contrib.auth.models import User

class RegisterItem(models.Model):
    name = models.CharField(max_length=120)
    Category = models.CharField(max_length=500)
    quantity = models.IntegerField(default=0)
    Price = models.IntegerField()


    def __str__(self):
        return  self.name


class Cart(models.Model):
    username=models.CharField(max_length=120)
    user_id=models.IntegerField()
    product_id=models.IntegerField()
    quantity=models.IntegerField(default=1)

    def __str__(self):
        return  self.username


class cust_details(models.Model):
    username=models.CharField(max_length=120)
    address=models.CharField(max_length=500)
    number=models.IntegerField()
    def __str__(self):
        return  self.username
