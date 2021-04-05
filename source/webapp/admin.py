from django.contrib import admin

from webapp.models import Product, Category, ProductInCart


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'remainder']
    list_filter = ['category', 'price']
    search_fields = ['name']
    fields = ['id', 'name', 'category', 'remainder', 'price']
    readonly_fields = ['id']


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductInCart, CartAdmin)
# Register your models here.
