from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import ScheduleListSerializer, ScheduleSerializer, UserSerializer
from .models import User, Schedule
from WTD.settings.base import SECRET_KEY
import jwt 

# Create your views here.
@api_view(['GET', 'POST'])
def schedule(request):
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
