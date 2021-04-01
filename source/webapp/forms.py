from django import forms
from django.forms import widgets

from webapp.models import category_choices


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=False, widget=widgets.Textarea, label='Описание')
    category = forms.ChoiceField(choices=category_choices, label='Категория')
    remainder = forms.IntegerField(required=True, min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=120, required=False, label='Искать')
