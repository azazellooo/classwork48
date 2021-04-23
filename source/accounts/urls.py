from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts.views import register_view

app_name = 'accounts'

urlpatterns = [
    path('ligin/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register')
]