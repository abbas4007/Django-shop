from rest_framework import serializers
from .models import Order
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

class CartAddSer(serializers.Serializer):
	quantity = serializers.IntegerField(min_value=1, max_value=9)
