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


class ProductInCart(models.Model):
    product = models.ForeignKey('webapp.Product',
                                related_name='product_in_cart',
                                verbose_name='продукт',
                                on_delete=models.CASCADE
                                )
    quantity = models.PositiveIntegerField(verbose_name='количество')


class UserData(models.Model):
    username = models.CharField(max_length=300, null=False, blank=False)
    phone_number = models.CharField(max_length=300, null=False, blank=False)
    address = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    product = models.ForeignKey('webapp.Product', related_name='order', on_delete=models.CASCADE, verbose_name='продукт')
    user_data = models.ForeignKey('webapp.UserData', related_name='users_order', verbose_name="Данные заказчика", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество')
# Create your models here.