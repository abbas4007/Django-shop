from django.urls import path
from .views import Registerview

app_name='accounts'

urlpatterns = [

    path('register/',Registerview.as_view(),name='register'),
]