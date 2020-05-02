# artices/urls.py
from django.urls import path
from . import views

urlpatterns = [
    #articles/
    path('articles/', views.index), #articles/
    path('articles/new/', views.new), #articles/new/
    path('articles/create/', views.create),

    ]