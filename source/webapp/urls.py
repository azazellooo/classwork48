from django.urls import path

from webapp.views.products import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)
from webapp.views.cart import ProductsInCartView, AddProductView, CartProductDelete, OrderView, OrderListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-view'),
    path('product/add', ProductCreateView.as_view(), name='product-add'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('cart/', ProductsInCartView.as_view(), name='cart'),
    path('cart/add/<int:pk>', AddProductView.as_view(), name='add-cart'),
    path('cart/delete/<int:pk>', CartProductDelete.as_view(), name='cart-product-delete'),
    path('order/', OrderView.as_view(), name='order'),
    path('order-list/', OrderListView.as_view(), name='order-list')
]