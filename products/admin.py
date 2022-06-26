from django.contrib import admin

from products.models import Product, Image


class ImageAdmin(admin.ModelAdmin):
    fields = ['image_tag']
    readonly_fields = ['image_tag']


admin.site.register(Image, ImageAdmin)
admin.site.register(Product)
