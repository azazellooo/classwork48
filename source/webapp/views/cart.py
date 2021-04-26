from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import ProductInCart, Product, Order, UserData
from webapp.forms import UserDataForm


class ProductsInCartView(View):
    template_name = 'cart/cart.html'
    order_form = UserDataForm

    def get(self, request):
        products_in_cart = ProductInCart.objects.all()
        session = request.session.get('cart', [])
        products_in_session = []
        for product in products_in_cart:
            if product.pk in session:
                products_in_session.append(product)
        tot = 0
        for i in products_in_session:
            tot += i.product.price * i.quantity
        return render(request, self.template_name, context={'cart_q': products_in_session, 'tot': tot, 'form': self.order_form})


class AddProductView(View):

    def get(self, request, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        session = request.session.get('cart', [])
        if product.remainder > 0:
            try:
                cart = ProductInCart.objects.get(product__pk=product.pk, pk__in=session)
                cart.quantity += 1
                cart.save()
            except ProductInCart.DoesNotExist:
                cart = ProductInCart.objects.create(product=product, quantity=1)
                session.append(cart.id)
                request.session['cart'] = session
            product.remainder -= 1
            product.save()
        else:
            return
        return redirect('product-list')


class CartProductDelete(View):

    def get(self, request, **kwargs):
        session = request.session.get('cart', [])
        request.session.modified = True
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        cart = ProductInCart.objects.get(product__pk=product.pk, pk__in=session)
        product = cart.product
        session.remove(cart.pk)
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
            order = Order.objects.create(quantity=pc.quantity, product=pc.product, user_data=u)
            if request.user.is_authenticated:
                order.user_object = request.user
                order.save()
            pc.delete()
        del request.session['cart']
        return redirect('product-list')


class OrderListView(LoginRequiredMixin, ListView):
    template_name = 'cart/order_list.html'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(user_object=self.request.user)