from django.urls import include, path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
app_name = 'accounts'
urlpatterns = [
	path('register/', views.UserRegisterView.as_view(), name='user_register'),
	path('registerapi/', views.UserRegisterApiView.as_view(), name='user_registerapi'),
	# path('verify/', views.UserRegisterVerifyCodeView.as_view(), name='verify_code'),
	path('login/', views.UserLoginView.as_view(), name='user_login'),
	path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),	]