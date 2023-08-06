from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.db.models import Count

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

import random
import datetime

# Create your views here.
@api_view(['GET'])
def new(request):
    today = datetime.date.today()
    new_movies = Movie.objects.filter(release_date__lte=today).order_by('-release_date')[:10]
    serializer = MovieSerializer(new_movies, many=True)
    # return HttpResponse(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recommendations(request, user_id):
    User = get_user_model()
    cur_user = get_object_or_404(User, id=user_id)
    cur_user_liked_movies = cur_user.liked_movies.all()
    # print(liked_movies)
    users = []
    for movie in cur_user_liked_movies:
        liked_users = movie.liked_users.all()
        for u in liked_users:
            if u not in users:
                users.append(u)
    # print(users)
    recommendations = []
    for user in users:
        liked_movies = user.liked_movies.all()
        for m in liked_movies:
            if m not in recommendations and m not in cur_user_liked_movies:
                recommendations.append(m)
    # print(recommendations)
    if len(recommendations) > 10:
        recommendations = recommendations.filter(genre__icontains=cur_user.favorite_genre).all()
        if len(recommendations) > 10:
            recommendations = random.sample(recommendations, 10)
        elif len(recommendations) < 10:
            cnt = 10 - len(recommendations)
            recommendations += random.sample(list(Movie.objects.filter(genre__icontains=cur_user.favorite_genre)), cnt)
    elif len(recommendations) < 10:
        cnt2 = 10 - len(recommendations)
        recommendations += random.sample(list(Movie.objects.filter(genre__icontains=cur_user.favorite_genre)), cnt2)
    elif len(recommendations) == 0:
        recommendations = random.sample(list(Movie.objects.filter(genre__icontains=cur_user.favorite_genre)), 10)
    serializer = MovieSerializer(recommendations, many=True)
    # return HttpResponse(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def popular(request):
    popular = Movie.objects.annotate(number_of_likes=Count('liked_users')).order_by('-number_of_likes')[:12]
    serializer = MovieSerializer(popular, many=True)
    # return HttpResponse(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            # 영화 평점 갱신
            review_cnt = Review.objects.filter(movie=movie).count()
            print(review_cnt)
            movie.rating = round(((movie.rating * (review_cnt - 1)) + int(request.data["score"])) / review_cnt, 2)
            movie.save()
            return Response(serializer.data)
    elif request.method == 'GET':
        reviews = Review.objects.filter(movie_id=movie_id).order_by('-id').all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request, movie_id, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method=="DELETE": 
        serializer = ReviewSerializer(review)
        if request.user == review.user:
            review.delete()
            reviews = Review.objects.filter(movie_id=movie_id).order_by('-id').all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)    

@api_view(['GET'])
def search(request, keyword):
    results = Movie.objects.filter(title__icontains=keyword).all()
    serializer = MovieSerializer(results, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if movie.liked_users.filter(id=request.user.pk).exists():
        movie.liked_users.remove(request.user)
    else:
        movie.liked_users.add(request.user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

