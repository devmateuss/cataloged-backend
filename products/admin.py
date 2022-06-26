from django.contrib import admin

from products.models import Product, Image


class ImageAdmin(admin.ModelAdmin):
    fields = ['thumbnail_preview']
    readonly_fields = ['thumbnail_preview']

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Imagem do produto'
    thumbnail_preview.allow_tags = True


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['images_list']
    fieldsets = (
        (None, {
            'fields': ('code', 'client', 'description', 'images', 'details', 'caracteristc')
        }),
        ('IMAGENS DO PRODUTO', {
            'fields': ('images_list',),
        }),
    )

    def images_list(self, obj):
        return obj.images_list

    images_list.short_description = ""
    images_list.allow_tags = True


admin.site.register(Image, ImageAdmin)
admin.site.register(Product, ProductAdmin)
