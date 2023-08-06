from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

# Token
import jwt
import bcrypt
from WTD.settings.base import SECRET_KEY

from .serializers import UserSerializer, UserListSerializer

from .models import User

@api_view(['POST'])
def login(request):
	# if User.objects.filter(email=request.data['email']).exists():   #스케줄 이동
	if User.objects.filter(email=request.data['email']).exists():   #스케줄 이동
		user = get_object_or_404(User, email=request.data['email'])
		serializer = UserSerializer(user)
		user_id = serializer.data['id']
		
		#토큰발행
		token = jwt.encode({'id' : user_id}, SECRET_KEY, algorithm = "HS256")
		token = token.decode('utf-8')       

		#제이슨 타입으로 리턴
		return JsonResponse({
			"token" : token,
			"userInfo" : serializer.data 
		})

	else:  #join 이동               
		return Response('0')


@api_view(['POST'])
def join(request):
	serializer = UserSerializer(data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save()
		user_id = serializer.data['id']

		#토큰발행
		token = jwt.encode({'id' : user_id}, SECRET_KEY, algorithm = "HS256")
		token = token.decode('utf-8')       

		#제이슨 타입으로 리턴, 홈 이동
		return JsonResponse({
			"token" : token,
			"userInfo" : serializer.data 
		})

	else:    #재입력 요청
		return Response('0')     


@api_view(['GET'])
def user(request):
	users = User.objects.all()
	serializer = UserListSerializer(users, many=True)
	name_list = []
	for user in serializer.data:
		name_list.append(user["nickname"])
	return_data = {
		"data" : serializer.data, 
		"name_list" : name_list
	}
	return Response(return_data)


@api_view(["PUT"])
def profile(request):
	token = request.META['HTTP_AUTHORIZATION']
	key = jwt.decode(token, SECRET_KEY, algorithm = 'HS256')
	user = get_object_or_404(User, id=int(key["id"]))

	serializer = UserSerializer(user, data=request.data)
	if serializer.is_valid(raise_exception=True):
		serializer.save(user=user)
		return Response(serializer.data)
#    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)