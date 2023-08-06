from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('review_create/', views.review_create, name='review_create'),
    path('<int:review_pk>/detail/', views.review_detail, name='review_detail'),
    path('<int:review_pk>/update/', views.review_update, name='review_update'),
    path('<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    path('<int:review_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:review_pk>/<int:comment_pk>/comment_delete/', views.comment_delete, name='comment_delete'),

]