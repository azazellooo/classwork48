from django.shortcuts import render

from webapp.models import Product


def index_view(request):
    products = Product.objects.order_by('category', 'name')
    return render(request, 'index.html', context={'products': products})


# Create your views here.
