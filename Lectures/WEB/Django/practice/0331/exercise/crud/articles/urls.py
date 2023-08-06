from django.urls import path
from . import views

urlpatterns = [
    path('articles/pong/', views.pong),
    path('articles/ping/', views.ping),

    ]