from django.contrib import admin

from .models import Product, Category, Brand

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'price', 'description')
# Register your models here.
admin.site.register(Product),
admin.site.register(Category),
admin.site.register(Brand)
