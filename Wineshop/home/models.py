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
