from django.conf import settings
from django.db import models
from django.utils import timezone


class Type(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()