from django.conf import settings
from django.db import models
from django.utils import timezone


class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    publish_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name