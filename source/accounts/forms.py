from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.CharField(required=True)

    # class Meta:
    #     fields = ('first_name', 'last_name', 'username', 'email')