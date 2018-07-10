from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Trap_Image, Trap, Insect
from .forms import ImageForm, InsectForm, TrapForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'classifier/index.html')

@login_required
def insects(request):
    insec = Insect.objects.all()

    return render(request, 'classifier/insect/main.html', {'insec': insec})

@login_required
def insect_new(request):
    if request.method == "POST":
        form = InsectForm(request.POST)
        if form.is_valid():
            insects = form.save()
            form = InsectForm()
            return HttpResponseRedirect(reverse('insects'))
    else:
        form = InsectForm()
    return render(request, 'classifier/insect/new.html', {'form': form})

@login_required
def insect_delete(request, pk):
    insect = get_object_or_404(Insect, pk=pk)
    insect.delete()
    return redirect('insects')

@login_required
def insect_detail(request, pk):
    insect = get_object_or_404(Insect, pk=pk)

    return render(request, 'classifier/insect/detail.html', {'insect': insect})

@login_required
def images(request):
    display_img = Trap_Image.objects.all()

    return render(request, 'classifier/image/main.html', {'display_img': display_img})

@login_required
def image_new(request):
    traps = Trap.objects.all()

    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save()
            return HttpResponseRedirect(reverse('images'))
    else:
        form = ImageForm()

    return render(request, 'classifier/image/new.html', {'form': form, 'traps': traps})

@login_required
def image_delete(request, pk):
    img = get_object_or_404(Trap_Image, pk=pk)
    img.delete()
    return redirect('images')

def image_detail(request, pk):
    img = get_object_or_404(Trap_Image, pk=pk)

    return render(request, 'classifier/image/detail.html', {'img': img})

@login_required
def traps(request):
    traps = Trap.objects.all()

    return render(request, 'classifier/trap/main.html', {'traps': traps})

@login_required
def trap_new(request):
    if request.method == "POST":
        form = TrapForm(request.POST)
        if form.is_valid():
            trap = form.save()
            return HttpResponseRedirect(reverse('traps'))
    else:
        form = TrapForm()

    return render(request, 'classifier/trap/new.html', {'form': form})

@login_required
def trap_delete(request, pk):
    trap = get_object_or_404(Trap, pk=pk)
    trap.delete()
    return redirect('traps')

@login_required
def trap_detail(request, pk):
    trap = get_object_or_404(Trap, pk=pk)

    return render(request, 'classifier/trap/detail.html', {'trap': trap})
