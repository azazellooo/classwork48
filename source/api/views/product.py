from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, SAFE_METHODS, AllowAny

from api.serializers import ProductSerializer
from webapp.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return super(ProductViewSet, self).get_permissions()
