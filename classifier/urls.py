from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('images/', views.images, name='images'),
    path('images/new/', views.image_new, name='image_new'),
    path('images/<int:pk>/', views.image_detail, name='image_detail'),
    path('images/delete/<int:pk>/', views.image_delete, name='image_delete'),
    path('insects/', views.insects, name='insects'),
    path('insects/new/', views.insect_new, name='insects_new'),
]
