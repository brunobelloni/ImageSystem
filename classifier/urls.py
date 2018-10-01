from django.urls import path

from . import views
from .views import (InsectCreateView, InsectDeleteView, InsectListView,
                    InsectUpdateView, TrapCreateView, TrapDeleteView,
                    TrapListView, TrapUpdateView)

app_name = 'classifier'

urlpatterns = [

]

# Insects
urlpatterns += [
    path('traps/', TrapListView.as_view(), name='trap_list'),
    path('traps/create/', TrapCreateView.as_view(), name='trap_create'),
    path('traps/<pk>/', TrapUpdateView.as_view(), name='trap_update'),
    path('traps/delete/<pk>', TrapDeleteView.as_view(), name='trap_delete'),
]

# Insects
urlpatterns += [
    path('insects/', InsectListView.as_view(), name='insect_list'),
    path('insects/create/', InsectCreateView.as_view(), name='insect_create'),
    path('insects/<pk>/', InsectUpdateView.as_view(), name='insect_update'),
    path('insects/delete/<pk>', InsectDeleteView.as_view(), name='insect_delete'),
]
