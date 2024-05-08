
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
]