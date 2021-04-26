from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login

from accounts.forms import UserRegisterForm
from webapp.models import Product, ProductInCart


class NewLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        session = request.session.get('cart', [])
        if len(session) >= 1:
            for cart_id in session:
                cart = ProductInCart.objects.get(pk=cart_id)
                product = Product.objects.get(pk=cart.product.pk)
                product.remainder += cart.quantity
                product.save()
        return super(NewLogoutView, self).dispatch(request, *args, **kwargs)


def register_view(request, **kwargs):
    context = {}
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product-list')
    context['form'] = form
    return render(request, 'registration/register.html', context=context)


# Create your views here.
