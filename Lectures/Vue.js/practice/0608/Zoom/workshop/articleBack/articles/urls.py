from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list),  #GET, POST/ articles/
    path('create/', views.create_article),
    path('<int:article_pk>', views.article_detail), #GET/ articles/:id/
]