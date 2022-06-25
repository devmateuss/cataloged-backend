from django.contrib import admin

from products.models import Product, Image

admin.site.register(Image)
admin.site.register(Product)
