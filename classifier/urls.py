from django.urls import path

from . import views as v

app_name = 'classifier'

urlpatterns = [
    path('', v.my_view, name='index'),
    path('search/', v.search, name='search'),
]


# Insects
urlpatterns += [
    path('insects/', v.InsectListView.as_view(), name='insect_list'),
    path('insects/create/', v.InsectCreateView.as_view(), name='insect_create'),
    path('insects/<pk>/', v.InsectUpdateView.as_view(), name='insect_update'),
    path('insects/delete/<pk>', v.InsectDeleteView.as_view(), name='insect_delete'),
]

# Traps
urlpatterns += [
    path('traps/', v.TrapListView.as_view(), name='trap_list'),
    path('traps/create/', v.TrapCreateView.as_view(), name='trap_create'),
    path('traps/<pk>/', v.TrapUpdateView.as_view(), name='trap_update'),
    path('traps/delete/<pk>', v.TrapDeleteView.as_view(), name='trap_delete'),
]

# Images
urlpatterns += [
    path('images/', v.ImageListView.as_view(), name='image_list'),
    path('images/create/', v.ImageCreateView.as_view(), name='image_create'),
    path('images/<pk>/', v.ImageUpdateView.as_view(), name='image_update'),
    path('images/delete/<pk>', v.ImageDeleteView.as_view(), name='image_delete'),
]

# Data
urlpatterns += [
    path('data/', v.DataListView.as_view(), name='data_list'),
    path('data/create/', v.DataCreateView.as_view(), name='data_create'),
    path('data/<pk>/', v.DataUpdateView.as_view(), name='data_update'),
    path('data/delete/<pk>', v.DataDeleteView.as_view(), name='data_delete'),
]
