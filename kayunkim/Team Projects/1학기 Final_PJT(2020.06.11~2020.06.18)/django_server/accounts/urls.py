from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 유저 정보
    path('user/', views.user, name='user'),

    # 유저가 좋아요한 영화 정보
    path('user/likes/<int:user_id>/', views.liked_list, name='liked_list'),

    # 유저와 생일 일치 영화 정보
    path('user/birthday/<int:user_id>/', views.birthday_list, name='birthday_list'),

    # path('<username>/follow/', views.follow, name='follow'),
]