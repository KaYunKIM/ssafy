from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .serializers import UserSerializer
from movies.models import Movie
from movies.serializers import MovieSerializer

import random

# Create your views here.
User = get_user_model()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user(request):
    user = get_object_or_404(User, username=request.user.username)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def liked_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    movies = user.liked_movies.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def birthday_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_birthday = user.date_of_birth
    birthday_month = user_birthday.month
    birthday_day = user_birthday.day
    movies = Movie.objects.filter(release_date=user_birthday).all()
    if len(movies) == 0:
        movies = random.sample(list(Movie.objects.filter(release_date__month=user_birthday.month, release_date__day=user_birthday.day).all()), 6)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


    

# @api_view(['POST'])
# # @permission_classes([IsAuthenticated])
# def follow(request, user_pk):
#     user = get_object_or_404(User, pk=user_pk)
#     if request.user != user:
#         # if serializer.followers.filter(pk=request.user.pk).exists():
#         if request.user in user.followers.all(): 
#             user.followers.remove(request.user)
#         else:
#             user.followers.add(request.user)
#         serializer = UserSerializer(user)  #id,username,followers
#         return Response(serializer.data)