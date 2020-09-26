from django.contrib import admin

from webapp.models import Product, Review


# class ProductAdmin(admin.ModelAdmin):
#     list_display_links = ['pk', 'name']


admin.site.register(Product)
admin.site.register(Review)
