from rest_framework import serializers

from webapp.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category', )
        read_only_fields = ('id', )

    def to_representation(self, instance):
        return instance.category
