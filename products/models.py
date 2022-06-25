from django.db import models

from user.models import Client


class Image(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)


class Product(models.Model):
    code = models.CharField(max_length=10)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=False, null=True)
    description = models.CharField(max_length=255, blank=False, null=False)
    images = models.ManyToManyField(Image)
    details = models.TextField()
    caracteristc = models.TextField()
