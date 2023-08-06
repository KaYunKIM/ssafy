from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from WTD.settings.base import SECRET_KEY
from .forms import AudioFileForm
from speech import STT
import jwt 

from .serializers import ProjectListSerializer, ProjectSerializer, MemberListSerializer, MemberSerializer
from .models import User, Project, Member, Audio

# Create your views here.
@api_view(['GET', 'POST'])
def project(request):
    token = request.META['HTTP_AUTHORIZATION']
    key = jwt.decode(token, SECRET_KEY, algorithm = 'HS256')
    user = get_object_or_404(User, id=int(key["id"]))

    if request.method =='GET':
        projects = Project.objects.all()
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data)

            # user_list = request.data["users"]
            # for user in user_list:
            #     cur_user = get_object_or_404(User, id=int(user))
            #     # member Create
            #     print(user, type(user), cur_user, user_list[user], len(user_list[user]))
            #     if len(user_list[user])>0:
            #         print("ooooo")
            #         member_serializer = MemberSerializer(project=project_serializer.data["id"], role=user_list[user])
            #         print("ok")
            #     else:
            #         print("xxxxxxx")
            #         member_serializer = MemberSerializer(project=project_serializer.data["id"])    
            #     print("========")
            #     if member_serializer.is_valid(raise_exception=True):
            #         print("222222222")
            #         member_serializer.save(user=cur_user)
            #         print("333333333")

            # # project Create
            

@api_view(['GET', 'POST'])
def member(request, project_id):
    # token = request.META['HTTP_AUTHORIZATION']
    # key = jwt.decode(token, SECRET_KEY, algorithm = 'HS256')
    # user = get_object_or_404(User, id=int(key["id"]))

    if request.method =='GET':
        members = Member.objects.all()
        serializer = MemberListSerializer(members, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        cur_project = get_object_or_404(Project, id=project_id)
        for user in request.data:
            cur_user = get_object_or_404(User, id=int(user))
            serializer = MemberSerializer(data=request.data[user])
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=cur_user, project=cur_project)
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def meetings(request, project_id):
    if request.method =='GET': 
       
        project = get_object_or_404(Project, id=project_id)

        meetings = project.meeting_set.all()
        serializer = MeetingSerializer(meetings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        project = get_object_or_404(Project, id=project_id)

        serializer = MeetingSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(project=project)
            return Response(serializer.data)

@api_view(['POST'])
def audio(request):
    form = AudioFileForm(request.POST, request.FILES)
    if form.is_valid():
        newform = Audio(audio=request.FILES['audio'])
        newform.save()
        return Response('1')
    return Response('0')

@api_view(['POST'])
def stt(request):
    file_path = request.data['title']
    stt = STT.STT()
    stt.file_load(file_path)
    sen1 , sen2 , sen3 = stt.speechtotext()

    return JsonResponse({
			"TitleList" : sen1,
			"HashTag" : sen2,
            "ToDoList" : sen3
		})
