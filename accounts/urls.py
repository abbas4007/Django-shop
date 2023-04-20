from django.urls import path
from .views import Registerview
from . import views

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
app_name='accounts'

urlpatterns = [

    path('register/',Registerview.as_view(),name='register'),
    # path('register/',Registerview.as_view(),name='register'),
    path('registerapi/', views.UserRegister.as_view()),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls