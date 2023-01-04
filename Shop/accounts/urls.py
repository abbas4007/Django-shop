from django.urls import include, path
from . import views
from  rest_framework.authtoken  import views as auth_view

app_name = 'accounts'
urlpatterns = [
	path('register/', views.UserRegisterView.as_view(), name='user_register'),
	path('registerapi/', views.UserRegisterApiView.as_view(), name='user_registerapi'),
	path('verify/', views.UserRegisterVerifyCodeView.as_view(), name='verify_code'),
	path('login/', views.UserLoginView.as_view(), name='user_login'),
	path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
	path('api-token-auth/', auth_view.obtain_auth_token)
	]