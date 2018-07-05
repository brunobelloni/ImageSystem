from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if not request.user.is_authenticated():
            return HttpResponseRedirect('login')

        # Code to be executed for each request/response after
        # the view is called.

        return response

@login_required
def index(request):
    return render(request, 'classifier/index.html')

def images(request):
    return render(request, 'classifier/images.html')

def insects(request):
    return render(request, 'classifier/insects.html')
