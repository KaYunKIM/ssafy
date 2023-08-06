from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('poll_create/', views.poll_create, name='poll_create'),
    path('<int:poll_pk>/poll_detail/', views.poll_detail, name='poll_detail'),
    path('<int:poll_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:poll_pk>/create_choice/<str:select>/', views.create_choice, name='create_choice'),
    path('random/', views.random, name='random'),

]
