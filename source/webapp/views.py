from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Product, category_choices
from webapp.forms import ProductForm


def index_view(request):
    products = Product.objects.order_by('category', 'name')
    return render(request, 'index.html', context={'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_view.html', context={'product': product})


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


def product_update_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'remainder': product.remainder,
            'price': product.price
        })
        return render(request, 'product_update.html', context={'product': product, 'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data.get('name')
            product.description = form.cleaned_data.get('description')
            product.category = form.cleaned_data.get('category')
            product.remainder = form.cleaned_data.get('remainder')
            product.price = form.cleaned_data.get('price')
            product.save()
            return redirect('product-view', pk=product.id)
        return render(request, 'product_update.html', context={'form': form, 'product': product})

# Create your views here.
