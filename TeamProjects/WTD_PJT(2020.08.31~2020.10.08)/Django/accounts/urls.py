from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    # 회원 인증
    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
    # 유저정보
    path('profile/', views.profile, name='profile')
]