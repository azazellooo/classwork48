from urllib.parse import urlencode

from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Product
from webapp.forms import ProductForm, SearchForm


class ProductListView(ListView):
    template_name = 'product-list.html'
    paginate_by = 7
    paginate_orphans = 2
    model = Product
    context_object_name = 'products'
    ordering = ('category', 'name')

    def get(self, request, **kwargs):
        self.search_form = SearchForm(request.GET)
        self.search_value = self.get_search_value()
        return super().get(request, kwargs)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search_value']
        return None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['search_form'] = self.search_form

        if self.search_value:
            context['query'] = urlencode({'search_value': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(name__icontains=self.search_value) |
                Q(description__icontains=self.search_value)
            )
        return queryset.exclude(remainder=0)


def product_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_view.html', context={'product': product})


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        categories = form.cleaned_data.pop('category')
        product = Product()
        for key, value in form.cleaned_data.items():
            setattr(product, key, value)

        product.save()
        product.category.set(categories)

        return super().form_valid(form)


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


def product_delete_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('product-list')


# Create your views here.
