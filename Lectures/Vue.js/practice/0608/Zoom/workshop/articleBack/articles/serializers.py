from rest_framework import serializers
from .models import Article
from accounts.serializers import UserSerializer

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'create_at']

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False) #is_valid 검증에서 pass
    class Meta:
        model = Article
        fields = '__all__'