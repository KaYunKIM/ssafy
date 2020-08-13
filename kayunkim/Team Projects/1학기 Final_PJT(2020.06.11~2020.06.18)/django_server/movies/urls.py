from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # 최신작 정보 url
    path('new/', views.new, name='new'),

    # 유저를 위한 추천작 정보 url
    path('recommendations/<int:user_id>/', views.recommendations, name='recommendations'),

    # 인기작 정보 url
    path('popular/', views.popular, name='popular'),

    # 영화 상세정보
    path('<int:movie_id>/', views.movie_detail, name="movie_detail"),

    # 한줄평 쓰기/가져오기
    path('<int:movie_id>/review/', views.review, name='review'),

    # 한줄평 삭제
    path('<int:movie_id>/review/<int:review_id>/', views.delete_review, name='delete_review'),

    # 영화 좋아요하기 
    path('like/<int:movie_id>/', views.like, name='like'),

    # 검색 결과 가져오기 
    path('<keyword>/', views.search, name='search'),

]