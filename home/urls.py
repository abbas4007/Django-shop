from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('',('home.urls', ,name='home')),
]
