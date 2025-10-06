from django.contrib import admin
from .models import Product, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'ordered_at', 'is_paid')
    list_filter = ('is_paid', 'ordered_at')
    inlines = [OrderItemInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
