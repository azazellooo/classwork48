from django.db import models

category_choices = [('other', 'Другое'),
                    ('laptops', 'Ноутбуки'),
                    ('tablets', 'Планшеты'),
                    ('accessories', 'аксессуары')]


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=False, blank=True)
    category = models.CharField(max_length=100, choices=category_choices, default='other')
    remainder = models.PositiveIntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

    def __str__(self):
        return f'{self.id}. {self.name}: {self.category}'
# Create your models here.
