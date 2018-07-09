from .forms import ImageForm, InsectForm, Trap, Insect
from .models import Trap_Image
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'classifier/index.html')


''' Insects '''
def insects(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    insec = Insect.objects.all()

    return render(request, 'classifier/insects.html', {'insec': insec})


def insect_new(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == "POST":
        form = InsectForm(request.POST)
        if form.is_valid():
            insects = form.save()
            form = InsectForm()
            return HttpResponseRedirect(reverse('insects'))
    else:
        form = InsectForm()
    return render(request, 'classifier/insect_new.html', {'form': form})

def insect_detail(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    insect = get_object_or_404(Insect, pk=pk)

    return render(request, 'classifier/image_detail.html', {'insect': insect})



''' Image '''
def images(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    display_img = Trap_Image.objects.all()

    return render(request, 'classifier/images.html', {'display_img': display_img})


def image_new(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    traps = Trap.objects.all()

    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save()
            return HttpResponseRedirect(reverse('images'))
    else:
        form = ImageForm()

    return render(request, 'classifier/image_new.html', {'form': form,

                                                         'traps': traps})
def image_delete(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    img = get_object_or_404(Trap_Image, pk=pk)
    img_pk = img.pk
    img.delete()
    return redirect('images')


def image_detail(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    img = get_object_or_404(Trap_Image, pk=pk)

    return render(request, 'classifier/image_detail.html', {'img': img})
