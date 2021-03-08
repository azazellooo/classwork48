from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product, category_choices
from webapp.forms import ProductForm


def index_view(request):
    products = Product.objects.order_by('category', 'name')
    return render(request, 'index.html', context={'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'task_view.html', context={'product': product})


def product_create_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_create.html', context={'choices': category_choices, 'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                category=form.cleaned_data.get('category'),
                remainder=form.cleaned_data.get('remainder'),
                price=form.cleaned_data.get('price')
            )
            return redirect('product-view', pk=product.id)
        return render(request, 'product_create.html', context={'form': form})

# Create your views here.
