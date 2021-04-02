from django.contrib import admin

from webapp.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'remainder']
    list_filter = ['category', 'price']
    search_fields = ['name']
    fields = ['id', 'name', 'category', 'remainder']
    readonly_fields = ['id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

# Register your models here.
