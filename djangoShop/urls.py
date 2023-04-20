
from django.contrib import admin
from django.urls import path,include

import accounts

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),
    path('account/',include('accounts.urls', namespace='accounts')),
    path('home/',include('home.urls', namespace='home')),
]
