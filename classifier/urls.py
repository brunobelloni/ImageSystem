from django.urls import path

from . import views
from .views import (InsectCreateView, InsectDeleteView, InsectListView,
                    InsectUpdateView)

app_name = 'classifier'

urlpatterns = [
    path('insects/', InsectListView.as_view(), name='insect_list'),
    path('insects/create/', InsectCreateView.as_view(), name='insect_create'),
    path('insects/<pk>/', InsectUpdateView.as_view(), name='insect_update'),
    path('insects/delete/<pk>', InsectDeleteView.as_view(), name='insect_delete'),
]
