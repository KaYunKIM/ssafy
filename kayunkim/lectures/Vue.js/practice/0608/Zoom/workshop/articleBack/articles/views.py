from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(reqeust):
    if request.method == 'POST':
        serilaizer = AricleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serilaizer.save()
            return Resposne(serilaizer.data)
        return Response(serializer.errors)

    elif request.method == 'GET':
        articles = Article.objects.all()
        serilaizer = AricleSerializer(articles, many=True)
        return Response(serilaizer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serilaizer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)  #NOT NULL CONSTRAINT FAILED
        return Response(serializer.data)
