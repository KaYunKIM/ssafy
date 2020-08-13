from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer, CommentSerializer
from .models import Article, Comment


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def article(request):
    if request.method=="GET":
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data) 


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk): 
    article = get_object_or_404(Article, pk=article_pk)
    if request.method=="GET":  #GET
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method=="PUT":    #UPDATE
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)    

    elif request.method=="DELETE":   #DELETE
        serializer = ArticleSerializer(article)
        if request.user == article.user:
            article.delete()            
            return Response(serializer.data)  

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method=="GET":
        # comments = article.comment_set.all
        comments = Comment.objects.filter(article_id = article_pk).all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)   


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, article_pk, comment_pk): 
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method=="DELETE": 
        serializer = CommentSerializer(comment)
        if request.user == comment.user:
            comment.delete()
            return Response(serializer.data)    