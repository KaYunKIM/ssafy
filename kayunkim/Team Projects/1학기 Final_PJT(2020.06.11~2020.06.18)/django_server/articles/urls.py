from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article, name='article'), #GET/POST
    path('<int:article_pk>/', views.article_detail, name='article_detail'), #GET/PUT/DELETE
    path('<int:article_pk>/comments/', views.comment, name='comment'), #GET/POST
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail, name='comment'), #DELETE
]