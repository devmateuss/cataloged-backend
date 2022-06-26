from django.db import models

from user.models import Client
from django.utils.html import format_html


class Image(models.Model):
    image = models.ImageField(upload_to='images/products')

    def __str__(self):
        return self.image.url

    def image_tag(self):
        return format_html('<img src="{}" />'.format(self.image.url))

    image_tag.short_description = 'Image'


class Product(models.Model):
    code = models.CharField(max_length=10)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=False, null=True)
    description = models.CharField(max_length=255, blank=False, null=False)
    images = models.ManyToManyField(Image)
    details = models.TextField()
    caracteristc = models.TextField()

    def __str__(self):
        return self.descriptionl