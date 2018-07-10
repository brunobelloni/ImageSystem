from django.shortcuts import render, redirect
from .models import Trap_Image, Trap, Insect
from .forms import ImageForm, InsectForm, TrapForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

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
            form.save()
            form = InsectForm()
            return redirect('insects')
    else:
        form = InsectForm()
    return render(request, 'classifier/insect/new.html', {'form': form})

@login_required
def insect_delete(request, pk):
    insect = Insect.objects.get(id=pk)
    insect.delete()
    return redirect('insects')

@login_required
def insect_detail(request, pk):
    insect = Insect.objects.get(id=pk)

    return render(request, 'classifier/insect/detail.html', {'insect': insect})

@login_required
def insect_edit(request, pk):
    insect = Insect.objects.get(id=pk)

    if request.method == "POST":
        form = InsectForm(request.POST, instance=insect)
        if form.is_valid():
            form.save()
            return redirect('insects')
    else:
        form = InsectForm(instance=insect)
    return render(request, 'classifier/insect/edit.html', {'form': form, 'insect': insect})

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
            form.save()
            return redirect('images')
    else:
        form = ImageForm()

    return render(request, 'classifier/image/new.html', {'form': form, 'traps': traps})

@login_required
def image_delete(request, pk):
    img = Trap_Image.objects.get(id=pk)
    img.delete()
    return redirect('images')

def image_detail(request, pk):
    img = Trap_Image.objects.get(id=pk)
    return render(request, 'classifier/image/detail.html', {'img': img})

def image_edit(request, pk):
    img = Trap_Image.objects.get(id=pk)
    traps = Trap.objects.all()

    if request.method == "POST":
        form = ImageForm(request.POST, instance=img)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = datetime.now()
            form.save()
            return redirect('images')
    else:
        form = ImageForm(instance=img)

    return render(request, 'classifier/image/edit.html', {'img': img, 'form': form, 'traps': traps})

@login_required
def traps(request):
    traps = Trap.objects.all()
    return render(request, 'classifier/trap/main.html', {'traps': traps})

@login_required
def trap_new(request):
    if request.method == "POST":
        form = TrapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traps')
    else:
        form = TrapForm()

    return render(request, 'classifier/trap/new.html', {'form': form})

@login_required
def trap_delete(request, pk):
    trap = Trap.objects.get(id=pk)
    trap.delete()
    return redirect('traps')

@login_required
def trap_detail(request, pk):
    trap = Trap.objects.get(id=pk)
    return render(request, 'classifier/trap/detail.html', {'trap': trap})

@login_required
def trap_edit(request, pk):
    trap = Trap.objects.get(id=pk)

    if request.method == "POST":
        form = TrapForm(request.POST, instance=trap)
        if form.is_valid():
            form.save()
            return redirect('traps')
    else:
        form = TrapForm(instance=trap)
    return render(request, 'classifier/trap/edit.html', {'form': form, 'trap': trap})
