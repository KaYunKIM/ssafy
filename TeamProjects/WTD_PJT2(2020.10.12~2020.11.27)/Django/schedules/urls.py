from django.urls import path
from . import views

app_name = 'schedules'

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'), #GET/POST
    path('<int:schedule_id>/', views.schedule_detail, name='schedule_detail'), # GET/PUT/DELETE
]