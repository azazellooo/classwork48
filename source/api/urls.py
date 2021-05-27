from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('order', views.order.OrderView.as_view(), name='order'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]