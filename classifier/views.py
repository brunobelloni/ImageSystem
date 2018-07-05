from .forms import ImageForm
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
    return render(request, 'classifier/insects.html')

def images(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        if request.method == "POST":
            image_form = ImageForm(request.POST)

            if image_form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                image = image_form.save()
            else:
                print(image_form.errors)
        else:
            image_form = ImageForm()
            
        return render(request, 'classifier/images.html', {'image_form': image_form})
