from django.views.generic import View, TemplateView
from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import ProductInCart, Product, Order, UserData
from webapp.forms import UserDataForm


class ProductsInCartView(View):
    template_name = 'cart/cart.html'
    order_form = UserDataForm

    def get(self, request):
        products_in_cart = ProductInCart.objects.all()
        tot = 0
        for i in products_in_cart:
            tot += i.product.price * i.quantity
        return render(request, self.template_name, context={'cart_q': products_in_cart, 'tot': tot, 'form': self.order_form})


class AddProductView(View):

    def get(self, request, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))

        if product.remainder > 0:
            try:
                cart = ProductInCart.objects.get(product__pk=product.pk)
                cart.quantity += 1
                cart.save()
            except ProductInCart.DoesNotExist:
                ProductInCart.objects.create(product=product, quantity=1)
            product.remainder -= 1
            product.save()
        else:
            return
        return redirect('product-list')


class CartProductDelete(View):

    def get(self, request, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        cart = ProductInCart.objects.get(product__pk=product.pk)
        product = cart.product
        product.remainder += cart.quantity
        product.save()
        cart.delete()
        return redirect('product-list')


class OrderView(View):

    def post(self, request, *args, **kwargs):
        products_in_cart = ProductInCart.objects.all()

        u = UserData.objects.create(
            username=request.POST.get('username'),
            address=request.POST.get('address'),
            phone_number=request.POST.get('phone_number')
        )
        for pc in products_in_cart:
            Order.objects.create(quantity=pc.quantity, product=pc.product, user_data=u)
            pc.delete()
        return redirect('product-list')
