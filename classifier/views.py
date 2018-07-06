from .forms import ImageForm, InsectForm
from .models import Trap_Image
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'classifier/index.html')

def insects(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == "POST":
        form = InsectForm(request.POST)
        if form.is_valid():
            insects = form.save()
            form = InsectForm()
    else:
        form = InsectForm()
    return render(request, 'classifier/insects.html', {'form': form})

def images(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save()
    else:
        form = ImageForm()
    return render(request, 'classifier/images.html', {'form': form})
