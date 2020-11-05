from rest_framework import serializers
from .models import User

# Create your models here.
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class UserListSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__' 