from django.urls import path, include

app_name = 'api'

product_urls = [
    path('')
]

urlpatterns = [
    path('', include(product_urls))
]