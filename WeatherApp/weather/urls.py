from django.contrib.auth import login
from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('login/', login, {'template_name': 'accounts/login.html'})
]
