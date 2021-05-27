from rest_framework import serializers

from api.serializers import OrderSerializer
from webapp.models import UserData, Product, Order


class UserDataSerializer(serializers.ModelSerializer):
    users_order = OrderSerializer(many=True)

    class Meta:
        model = UserData
        fields = ('username', 'phone_number', 'address', 'users_order')
        read_only_fields = ('id', 'created_at', )

    def create(self, validated_data):
        username = validated_data.get('username')
        phone_number = validated_data.get('phone_number')
        address = validated_data.get('address')
        user_data = UserData.objects.create(username=username, phone_number=phone_number, address=address)
        users_orders = validated_data.get('users_order')
        for users_order in users_orders:
            product = Product.objects.get(pk=users_order.get('product').pk)
            Order.objects.create(product=product, quantity=users_order.get('quantity'), user_data=user_data)
        return user_data
