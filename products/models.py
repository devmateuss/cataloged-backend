from django.db import models

from user.models import Client
from django.utils.html import mark_safe


class Image(models.Model):
    image = models.ImageField(upload_to='images/products')

    def __str__(self):
        return self.image.url

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""


class Product(models.Model):
    code = models.CharField(max_length=10)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=False, null=True)
    description = models.CharField(max_length=255, blank=False, null=False)
    images = models.ManyToManyField(Image)
    details = models.TextField()
    caracteristc = models.TextField()

    def __str__(self):
        return self.description

    @property
    def images_list(self):
        if self.images:
            html = ""
            for image in self.images.all():
                html += '<img src="{}" width="300" height="300" />'.format(image.image.url) + " "

            tag = '<a href="#" class="image">' + html + '</a>'
            return mark_safe(tag)
        return ""