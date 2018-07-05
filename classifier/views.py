from .forms import ImageForm
from .models import Trap_Image
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'classifier/index.html')

def images(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'classifier/images.html')

def insects(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'classifier/insects.html')

class CreateImageView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'classifier/images.html'

    form_class = ImageForm
    model = Trap_Image
