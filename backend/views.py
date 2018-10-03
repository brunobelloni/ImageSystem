from django.contrib.auth.views import LoginView


class MeuLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
