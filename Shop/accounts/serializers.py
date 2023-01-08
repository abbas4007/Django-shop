from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','phone_number','full_name','password')

    
    def create(self, validated_data):
        # del validated_data['password2']
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):

    class  Meta:
        model=User
        fields=('phone','password')