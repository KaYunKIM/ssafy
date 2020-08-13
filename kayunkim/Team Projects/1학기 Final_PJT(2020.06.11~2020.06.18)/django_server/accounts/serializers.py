from rest_auth.registration.serializers import RegisterSerializer

from rest_framework import serializers
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()  

class CustomRegisterSerializer(RegisterSerializer):

    date_of_birth = serializers.DateField(input_formats=["%Y-%m-%d"], required=True, write_only=True)
    favorite_genre = serializers.CharField(write_only=True, required=True)

    def get_cleaned_data(self):
        # print('get_cleaned_data')
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'date_of_birth': self.validated_data.get('date_of_birth', ''),
            'favorite_genre': self.validated_data.get('favorite_genre', ''),
        }

    def save(self, request):
        user = super().save(request)
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.favorite_genre = self.cleaned_data.get('favorite_genre')
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 