from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('<int:movie_pk>/review_create/', views.review_create, name='review_create'),
    path('<int:movie_pk>/review/<int:review_pk>/review_detail/', views.review_detail, name='review_detail'),
    path('<int:movie_pk>/review/<int:review_pk>/review_edit/',views.review_edit, name='review_edit'),
    path('<int:movie_pk>/review/<int:review_pk>/review_delete/', views.review_delete, name='review_delete'),
    path('<int:movie_pk>/review/<int:review_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:movie_pk>/review/<int:review_pk>/<int:comment_pk>/comment_edit/',views.comment_edit, name='comment_edit'),
    path('<int:movie_pk>/review/<int:review_pk>/<int:comment_pk>/comment_delete/', views.comment_delete, name='comment_delete'),
    path('recommend/', views.recommend, name='recommend'),
]