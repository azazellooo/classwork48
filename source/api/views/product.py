from rest_framework import viewsets

from api.serializers import ProductSerializer
from webapp.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
