from django.urls import path
from django.contrib.auth.views import LoginView

from accounts.views import register_view, NewLogoutView

app_name = 'accounts'

urlpatterns = [
    path('ligin/', LoginView.as_view(), name='login'),
    path('logout/', NewLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register')
]