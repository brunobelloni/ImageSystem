from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from .views import MeuLoginView

app_name = 'backend'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MeuLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('classifier/', include('classifier.urls')),
]
