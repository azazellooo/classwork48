from rest_framework import serializers

from webapp.models import Product
from api.serializers.category import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'remainder', 'price', )
        read_only_fields = ('id',)

