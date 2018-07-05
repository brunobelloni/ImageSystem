from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('images/', views.CreateImageView.as_view(), name='images'),
    path('insects/', views.insects, name='insects'),
]
