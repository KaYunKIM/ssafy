from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import serializers 
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
from WTD.settings.base import SECRET_KEY
from .forms import AudioFileForm
from speech import STT
from django.db.models import Q
import jwt, datetime, json

from .serializers import ProjectListSerializer, ProjectSerializer, MemberListSerializer, MemberSerializer, MeetingSerializer, MeetingListSerializer, TaskListSerializer, TaskSerializer, KeywordSerializer
from .models import User, Project, Member, Audio, Task, Keyword,  Meeting

# Create your views here.
@api_view(['GET', 'POST'])
def project(request):
    if request.method =='GET':
        token = request.META['HTTP_AUTHORIZATION']
        key = jwt.decode(token, SECRET_KEY, algorithm = 'HS256')
        user = get_object_or_404(User, id=int(key["id"]))

        projects = user.project_set.all()
        serializer = ProjectListSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': 
        project_serializer = ProjectSerializer(data=request.data)
        if project_serializer.is_valid(raise_exception=True):
            project_serializer.save()
            
            # member테이블 저장
            cur_project = get_object_or_404(Project, id=project_serializer.data["id"])

            # serializer = MemberSerializer(data=request.data["members"], many=True) #user 접근 불가
            for user in request.data["members"]:
                cur_user = get_object_or_404(User, nickname=user["nickname"])
                member_serializer = MemberSerializer(data=user)
                if member_serializer.is_valid(raise_exception=True):
                    member_serializer.save(user=cur_user, project=cur_project)
            return Response(project_serializer.data)


@api_view(['DELETE'])
def project_detail(request, project_id): 
    project = get_object_or_404(Project, pk=project_id)
    serializer = ProjectSerializer(project)
    project.delete()            
    return Response(serializer.data)  


@api_view(['GET', 'DELETE'])
def member(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'GET':
        members = Member.objects.filter(project=project_id)
        serializer = MemberListSerializer(members, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        token = request.META['HTTP_AUTHORIZATION']
        key = jwt.decode(token, SECRET_KEY, algorithm = 'HS256')
        user = get_object_or_404(User, id=int(key["id"]))

        member = get_object_or_404(Member, user=user, project=project)
        serializer = MemberSerializer(member)
        member.delete()            
        return Response(serializer.data)  


@api_view(['GET'])
def member_task_list(request, project_id, nickname, meeting_date):    
    meetings = Meeting.objects.filter(project_id=project_id)
    # print(meetings)
    
    if not meetings:
        return Response(status = status.HTTP_400_BAD_REQUEST)

    q = Q()

    for meeting in meetings: 
        print(meeting.id)
        q.add(Q(meeting_id=meeting.id), q.OR)
    
    # 매니저 이름이 현재 유저인 and조건 넣기
    q.add(Q(manager=nickname),q.AND)
    
    # 해당 날짜의 task
    time_list = meeting_date.split('-')
    datetime_filter = datetime.datetime(int(time_list[0]),int(time_list[1]),int(time_list[2]))
    q.add(Q(start_time__startswith=datetime_filter.date()), q.AND)        
    
    tasks = Task.objects.filter(q)
    serializer = TaskListSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def meeting(request, project_id, meeting_date): 
    if request.method =='GET':
        # 프로젝트를 가져온다 (해당하는 아이디에 관련된 프로젝트를 가져온다)
        project = get_object_or_404(Project, id=project_id)
        project_title = project.title
        
        time_list = meeting_date.split('-')
        start_datetime_filter = datetime.datetime(int(time_list[0]),int(time_list[1]),int(time_list[2]), 00, 00, 00)
        end_datetime_filter = datetime.datetime(int(time_list[0]),int(time_list[1]),int(time_list[2]), 23,59,59)
        print(start_datetime_filter)
        meetings = Meeting.objects.filter(project_id=project_id, time__range=[start_datetime_filter, end_datetime_filter]).order_by('-time')
        
        dataList = []

        for meeting in meetings:
            meetingList = {}
            meetingList['id'] = meeting.id
            meetingList['project_id'] = meeting.project_id
            meetingList['title'] = meeting.title
            meetingList['time'] = meeting.time
            meetingList['origin_text'] = meeting.origin_text
            meetingList['summary'] = meeting.summary
            keywordList = []
            keywords = meeting.keywords.all()
            for keyword in keywords:
                keywordList.append(keyword.title)
            meetingList['keyword'] = keywordList
            
            dataList.append(meetingList)
      
        # 미팅 리스트를 반환
        return JsonResponse({
            "projectTitle": project_title,
            "meetingList": dataList
        }, safe=False)
  
    elif request.method =='POST':
        project = get_object_or_404(Project, id=project_id)
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(project=project)
            return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    keywords = meeting.keywords.all()
    
    if request.method == 'GET':
        serializer = MeetingSerializer(meeting)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MeetingSerializer(meeting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        for keyword in keywords:
            keyword.delete()
            
        meeting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 파일 업로드 > 모델 돌려서 결과 반환 > post로 데이터 저장
@api_view(['POST'])
def meeting_info(request, meeting_id):

    # 해당하는 미팅을 가져온다
    meeting = get_object_or_404(Meeting, id=meeting_id)
    
    # 해당 미팅과 연결된 프로젝트
    project_id = meeting.project_id
    project = get_object_or_404(Project, id=project_id)

    # 회의 요약 내용
    summary = ""
    idx = 1

    for sentence in request.data["summary"]:
        if sentence == "":
            continue
        summary += ("[ " + str(idx) + " ] " + sentence+"\n")
        idx+=1

    meeting.summary = summary 
    meeting.save()

    # 키워드 keyword테이블에 create
    for keyword in request.data["keyword"]:
        keyword_data = Keyword.objects.create(title=keyword)
        meeting.keywords.add(keyword_data)
        
    # 할 일 리스트 create 하기
    for toDo in request.data["toDoList"]:
        Task.objects.create(meeting=meeting, title=toDo)
    
    return Response('success')

@api_view(['POST'])
def audio(request):
    form = AudioFileForm(request.POST, request.FILES)
    if form.is_valid():
        newform = Audio(audio=request.FILES['audio'])
        newform.save()
        title = str(newform.audio)
        print(title)
        return HttpResponse(title)
    return Response('0')

@api_view(['POST'])
def stt(request):
    file_path = request.data['title']
    stt = STT.STT()
    stt.file_load(file_path)
    sen1 , sen2 , sen3 = stt.speechtotext()

    return JsonResponse({
	    "summary" : sen1,
		"keyword" : sen2,
        "toDoList" : sen3
	})


@api_view(['POST'])
def realtime_stt(request):
    stt = STT.STT()
    
    # 해당하는 미팅을 가져온다
    meeting_id = request.data['meetingId']
    origin_text = request.data['text']
    print(origin_text)
    if len(origin_text) == 0:
        return Response("회의 내용이 없습니다", status = status.HTTP_400_BAD_REQUEST)

    meeting = get_object_or_404(Meeting, id=meeting_id)
    meeting.origin_text = origin_text
    meeting.save()

    sen1 , sen2 , sen3 = stt.get_tasklist(origin_text)

    return JsonResponse({
		"summary" : sen1,
		"keyword" : sen2,
        "toDoList" : sen3
	})

@api_view(['GET'])
def all_task_list(request, project_id):
    # 그 유저 가져오기
    token = request.META['HTTP_AUTHORIZATION']
    key = jwt.decode(token, SECRET_KEY, algorithm = 'HS256')
    user = get_object_or_404(User, id=int(key["id"]))

    # 그 프로젝트에 해당하는 모든 미팅을 가져오기
    meetings = Meeting.objects.filter(project_id=project_id)
    if not meetings:
        return Response(status = status.HTTP_400_BAD_REQUEST)

    q = Q()
    # 그 미팅에 있는 meeting_id or조건으로 query 만들기            
    for meeting in meetings: 
        print(meeting.id)
        q.add(Q(meeting_id=meeting.id), q.OR)
    
    # 매니저 이름이 현재 유저인 and조건 넣기
    q.add(Q(manager=user.nickname),q.AND)
    
    # 그 쿼리 조건으로 task뽑기
    tasks = Task.objects.filter(q)

    serializer = TaskListSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        task.title = request.data["title"]
        
        serializer = TaskSerializer(task, data=request.data)
        
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def task_list(request, project_id, meeting_date):
    
    time_list = meeting_date.split('-')
    start_datetime_filter = datetime.datetime(int(time_list[0]),int(time_list[1]),int(time_list[2]), 00, 00, 00)
    end_datetime_filter = datetime.datetime(int(time_list[0]),int(time_list[1]),int(time_list[2]), 23,59,59)
    print(start_datetime_filter)
    meetings = Meeting.objects.filter(project_id=project_id, time__range=[start_datetime_filter, end_datetime_filter]).order_by('-time')

    q = Q()
    
    # 그 미팅에 있는 task를 다 가져와서 리스트로 저장한다
    # allTaskList = []
    for meeting in meetings: 
        q.add(Q(meeting_id=meeting.id), q.OR)
    
    tasks = Task.objects.filter(q)
    
    serializer = TaskListSerializer(tasks , many=True)
    return Response(serializer.data)
    # return Response(0)

@api_view(['GET'])
def keyword_search(request, keyword):
    token = request.META['HTTP_AUTHORIZATION']
    key = jwt.decode(token, SECRET_KEY, algorithm = 'HS256')
    user = get_object_or_404(User, id=int(key["id"]))
    
    # 키워드를 포함된 애들을 찾는다
    keywords = Keyword.objects.filter(title__icontains=keyword)
    
    # 해당 키워드가 포함된 미팅 리스트를 찾는다
    meeting_list = []
    for keyword in keywords:
        meetings = keyword.meeting_set.all()
        for meeting in meetings:
            meeting_list.append(meeting)
    
    meetings = []
    for meeting in meeting_list:
        project_id = meeting.project_id
        members = Member.objects.filter(project_id=project_id)
        for member in members:
            if member.user_id == user.id:
                meetings.append(meeting)
                break
   
    serializer = MeetingListSerializer(meetings, many=True)

    return Response(serializer.data)