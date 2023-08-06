from rest_framework import serializers

from .models import Movie, Review
from accounts.serializers import UserSerializer

class MovieSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    movie = MovieSerializer(required=False)
    # like_users = UserSerializer(required=False, read_only=True, many=True)
    class Meta:
        model = Review
        fields = '__all__'