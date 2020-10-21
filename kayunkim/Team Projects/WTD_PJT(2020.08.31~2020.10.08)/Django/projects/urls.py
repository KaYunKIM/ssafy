from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    # projects
    path('', views.project, name='project'), #GET/POST
    # members
    path('<int:project_id>/members/', views.member, name='member'), #GET/POST
    # meetings
    path('<int:project_id>/meetings/', views.meetings, name='meetings'),
    # audio
    path('audio/', views.audio, name='audio'), #POST
    # stt
    path('stt/', views.stt, name='stt'), #POST
]