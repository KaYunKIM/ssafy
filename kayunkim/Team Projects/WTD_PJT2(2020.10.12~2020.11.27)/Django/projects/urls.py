from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # projects
    path('', views.project, name='project'), #GET/POST
    path('<int:project_id>/', views.project_detail, name='project_detail'), #DELETE

    # members
    path('<int:project_id>/members/', views.member, name='member'), #GET/DELETE

    # member_task_list
    path('<int:project_id>/<str:nickname>/<str:meeting_date>/member_task_list/', views.member_task_list, name='member_task_list'), #GET


    # meetings
    path('<int:project_id>/<str:meeting_date>/meeting/', views.meeting, name='meeting'), #GET/POST
    path('<int:meeting_id>/meeting_detail/', views.meeting_detail, name='meeting_detail'), # GET/PUT/DELETE

    # audio
    path('audio/', views.audio, name='audio'), #POST
    
    # stt
    path('stt/', views.stt, name='stt'), #POST
    
    # stt
    path('stt/real_time/', views.realtime_stt, name='realtime_stt'), #POST

    # meeting_info 
    # Description: 모델 결과 (요약, 키워드, task 저장)
    path('<int:meeting_id>/meeting_info/', views.meeting_info, name='meeting_info'), #POST

    # all_task_list 
    # Description: 특정 user의 모든 task
    path('<int:project_id>/all_task_list/', views.all_task_list, name='all_task_list'), #GET

    # task
    path('<int:task_id>/task_detail/', views.task_detail, name='task_detail'), #GET/PUT/DELETE

    # task_list
    # Description: 특정 프로젝트의 task 리스트
    path('<int:project_id>/<str:meeting_date>/task_list/', views.task_list, name='task_list'), #GET
    
    # keyword search
    path('search/<str:keyword>/', views.keyword_search, name='keyword_search') #GET
]
