from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=False, blank=True)
    category = models.ManyToManyField('webapp.Category', related_name='products', db_table='product_categories')
    remainder = models.PositiveIntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return f'{self.id}. {self.name}: {self.category}'


class Category(models.Model):
    category = models.CharField(max_length=150, default='other', verbose_name='Категория')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category

# Create your models here.
