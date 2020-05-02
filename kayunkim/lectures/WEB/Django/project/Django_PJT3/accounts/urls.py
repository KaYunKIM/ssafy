from django.urls import path
from . import views

app_name='accounts'

urlpatterns=[
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('<int:user_pk>/delete/', views.delete_user, name='delete_user'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/detail/', views.detail, name='detail'),
]