from django.db import models
from django.contrib.auth import get_user_model


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

    def get_total(self):
        return self.quantity * self.product.price


class UserData(models.Model):
    username = models.CharField(max_length=300, null=False, blank=False)
    phone_number = models.CharField(max_length=300, null=False, blank=False)
    address = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user_object = models.ForeignKey(
                                    get_user_model(),
                                    related_name='order',
                                    on_delete=models.CASCADE,
                                    verbose_name='Пользователь',
                                    null=True,
                                    blank=True
                                    )

    def get_tot(self):
        tot = 0
        for i in self.users_order.all():
            tot += i.get_sum()
        return tot


class Order(models.Model):
    product = models.ForeignKey('webapp.Product',
                                related_name='order',
                                on_delete=models.CASCADE,
                                verbose_name='продукт'
                                )
    user_data = models.ForeignKey('webapp.UserData',
                                  related_name='users_order',
                                  verbose_name="Данные заказчика",
                                  on_delete=models.CASCADE
                                  )
    quantity = models.PositiveIntegerField(verbose_name='количество')

    def get_sum(self):
        return self.quantity * self.product.price

# Create your models here.