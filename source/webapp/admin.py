from django.contrib import admin

from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'remainder']
    list_filter = ['category', 'price']
    search_fields = ['name']
    fields = ['id', 'name', 'category', 'remainder']
    readonly_fields = ['id']


admin.site.register(Product, ProductAdmin)


# Register your models here.
