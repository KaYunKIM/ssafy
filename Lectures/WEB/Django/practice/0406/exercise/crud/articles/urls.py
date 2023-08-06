from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:pk>/', views.detail),     #/articles/{{ article.pk }}/
    path('<int:pk>/delete/', views.delete),      #/articles/{{ article.pk }}/delete
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),

]
