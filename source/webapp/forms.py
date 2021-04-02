from django import forms

from webapp.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'remainder', 'price')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=120, required=False, label='Искать')
