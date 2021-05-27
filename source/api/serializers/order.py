from rest_framework import serializers

from webapp.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('product', 'quantity', )
        read_only_fields = ('id',)



