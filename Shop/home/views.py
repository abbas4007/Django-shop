from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product,Category
from rest_framework.views import APIView
from rest_framework.response  import Response
from .serializers import ProductSerializer
class HomeView(View):
	#bray inke momkene category ha filter bshan pas None ersal mikonim
	def get(self, request, category_slug=None):
		products = Product.objects.filter(available=True)
		categories = Category.objects.filter(is_sub=False)
		if category_slug:
			category = Category.objects.get(slug=category_slug)
			products = products.filter(category=category)
		return render(request, 'home/home.html', {'products':products, 'categories':categories})	

class HomeApiView(APIView):
	# serializer_class=ProductSerializer
	def get(self,request):
		product=Product.objects.all()
		ser_data=ProductSerializer(product,many=True)
		return Response(data=ser_data.data)

class ProductDetailView(View):
	def get(self, request, slug):
		product = get_object_or_404(Product, slug=slug)
		return render(request, 'home/detail.html', {'product':product})