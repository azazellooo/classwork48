# Generated by Django 3.1.7 on 2021-04-05 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_productincart'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('phone_number', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='webapp.product', verbose_name='продукт')),
                ('user_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_order', to='webapp.userdata', verbose_name='Данные заказчика')),
            ],
        ),
    ]
