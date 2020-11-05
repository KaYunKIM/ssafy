from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import ScheduleListSerializer, ScheduleSerializer, UserSerializer
from .models import User, Schedule
from WTD.settings.base import SECRET_KEY
import jwt 

    
# Create your views here.
@api_view(['GET', 'POST'])
def schedule_list(request):
    token = request.META['HTTP_AUTHORIZATION']
    key = jwt.decode(token, SECRET_KEY, algorithm = 'HS256')
    user = get_object_or_404(User, id=int(key["id"]))

    if request.method =='GET':
        schedules = user.schedule_set.all()
        serializer = ScheduleListSerializer(schedules, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # user_serializer = UserSerializer(user)
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def schedule_detail(request, schedule_id):
    # 유저
    token = request.META['HTTP_AUTHORIZATION']
    key = jwt.decode(token, SECRET_KEY, algorithm = 'HS256')
    user = get_object_or_404(User, id=int(key["id"]))

    # 스케쥴
    schedule = get_object_or_404(Schedule, id=schedule_id)

    if request.method == 'GET':
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ScheduleSerializer(schedule, data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
