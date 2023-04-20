from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('list-api/', views.Home.as_view(), name='list'),
    path('bucket/', views.BucketView.as_view(),name='bucket'),

    # path('category/<slug:category_slug>/', views.HomeView.as_view(), name='category_filter'),
    # path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),

]