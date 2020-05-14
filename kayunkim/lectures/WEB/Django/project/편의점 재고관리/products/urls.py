from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:store_pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/create/', views.create, name='create'),
    path('<int:store_pk>/<int:item_pk>/item_detail', views.item_detail, name='item_detail'),
    path('<int:store_pk>/<int:item_pk>/edit', views.edit, name='edit'),
    path('<int:store_pk>/<int:item_pk>/delete', views.delete, name='delete'),
]