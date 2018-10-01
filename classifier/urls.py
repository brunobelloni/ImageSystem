from django.urls import path

from . import views
from .views import InsectListView

app_name = 'classifier'

urlpatterns = [
    path('', InsectListView.as_view(), name='insect_view'),
]
