from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('images/', views.images, name='images'),
    path('images/new/', views.image_new, name='image_new'),
    path('images/<int:pk>/', views.image_detail, name='image_detail'),
    path('images/edit/<int:pk>/', views.image_edit, name='image_edit'),
    path('images/delete/<int:pk>/', views.image_delete, name='image_delete'),
    path('images/new_data_img/', views.image_new_data, name='image_new_data'),
    path('insects/', views.insects, name='insects'),
    path('insects/new/', views.insect_new, name='insect_new'),
    path('insects/<int:pk>/', views.insect_detail, name='insect_detail'),
    path('insects/edit/<int:pk>/', views.insect_edit, name='insect_edit'),
    path('insects/delete/<int:pk>/', views.insect_delete, name='insect_delete'),
    path('traps/', views.traps, name='traps'),
    path('traps/new/', views.trap_new, name='trap_new'),
    path('traps/<int:pk>/', views.trap_detail, name='trap_detail'),
    path('traps/edit/<int:pk>/', views.trap_edit, name='trap_edit'),
    path('traps/delete/<int:pk>/', views.trap_delete, name='trap_delete'),
    path('variables/', views.variables, name='variables'),
    path('variables/new/', views.variable_new, name='variable_new'),
    path('variables/<int:pk>/', views.variable_detail, name='variable_detail'),
    path('variables/edit/<int:pk>/', views.variable_edit, name='variable_edit'),
    path('variables/delete/<int:pk>/', views.variable_delete, name='variable_delete'),
    path('data/', views.view_data, name='data'),
    path('data/new/', views.data_new, name='data_new'),
    path('data/<int:pk>/', views.data_detail, name='data_detail'),
    path('data/edit/<int:pk>/', views.data_edit, name='data_edit'),
    path('data/delete/<int:pk>/', views.data_delete, name='data_delete'),

    path('teste/', views.teste, name='teste'),
]
