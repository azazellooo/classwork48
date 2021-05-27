from rest_framework import serializers

from webapp.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'remainder', 'price', )
        read_only_fields = ('id',)
