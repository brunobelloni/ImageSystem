from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('images/', views.images, name='images'),
    path('images/new', views.image_new, name='image_new'),
    path('insects/', views.insects, name='insects'),
]
