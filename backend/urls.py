from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(redirect_authenticated_user=True,
                               template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('classifier/', include('classifier.urls')),
]
