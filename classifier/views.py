from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template import loader

from .forms import DataForm, ImageForm, InsectForm, TrapForm, VariableForm
from .models import Insect, Trap, Trap_Image, Trap_Image_Data, Variable
from .opencv_library import get_cropped_img, set_data_img


@login_required
def index(request):
    unclassified_data = Trap_Image_Data.objects.order_by(
        'id').filter(insect=None)
    quantity = int(len(Trap_Image_Data.objects.filter(
        insect=None)) / len(Variable.objects.all()))
    first = None

    try:
        first = unclassified_data[0]
        b64 = first.image.image
        x, y = first.x, first.y
        img = get_cropped_img(b64=b64, x=x, y=y, margin=50)
    except Exception as e:
        img = None

    try:
        insects = Insect.objects.order_by('id')
    except Exception as e:
        insects = None

    dict = {'unclassified_data': unclassified_data, 'quantity': quantity,
            'img': img, 'insects': insects, 'data': first}
    return render(request, 'classifier/index.html', dict)


def set_teste(request, id, x, y):
    insect = Insect.objects.get(id=id)
    data = Trap_Image_Data.objects.filter(x=x).filter(y=y)

    for d in data:
        d.insect = insect
        d.save()

    return redirect('index')


def delete_teste(request, x, y):
    data = Trap_Image_Data.objects.filter(x=x).filter(y=y)

    for d in data:
        d.delete()

    return redirect('index')


##########################
## Functions to Insects ##
##########################

@login_required
def insects(request):
    insec = Insect.objects.order_by('id')
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

    dict = {'form': form, 'insect': insect}
    return render(request, 'classifier/insect/edit.html', dict)


#########################
## Functions to Images ##
#########################

@login_required
def images(request):
    display_img = Trap_Image.objects.order_by('id')
    dict = {'display_img': display_img}
    return render(request, 'classifier/image/main.html', dict)


@login_required
def image_new(request):
    traps = Trap.objects.order_by('id')

    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('images')
    else:
        form = ImageForm()

    dict = {'form': form, 'traps': traps}
    return render(request, 'classifier/image/new.html', dict)


@login_required
def image_new_data(request):
    traps = Trap.objects.order_by('id')

    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            img = form['image'].value()
            id = form.save()
            set_data_img(img, id)
            return redirect('images')
    else:
        form = ImageForm()

    dict = {'form': form, 'traps': traps}
    return render(request, 'classifier/image/new.html', dict)


@login_required
def image_delete(request, pk):
    img = Trap_Image.objects.get(id=pk)
    img.delete()
    return redirect('images')


def image_detail(request, pk):
    img = Trap_Image.objects.get(id=pk)
    dict = {'img': img}
    return render(request, 'classifier/image/detail.html', dict)


def image_edit(request, pk):
    img = Trap_Image.objects.get(id=pk)
    traps = Trap.objects.order_by('id')

    if request.method == "POST":
        form = ImageForm(request.POST, instance=img)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = datetime.now()
            form.save()
            return redirect('images')
    else:
        form = ImageForm(instance=img)

    dict = {'img': img, 'form': form, 'traps': traps}
    return render(request, 'classifier/image/edit.html', dict)

########################
## Functions to Traps ##
########################


@login_required
def traps(request):
    traps = Trap.objects.order_by('id')
    dict = {'traps': traps}
    return render(request, 'classifier/trap/main.html', dict)


@login_required
def trap_new(request):
    if request.method == "POST":
        form = TrapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('traps')
    else:
        form = TrapForm()

    dict = {'form': form}
    return render(request, 'classifier/trap/new.html', dict)


@login_required
def trap_delete(request, pk):
    trap = Trap.objects.get(id=pk)
    trap.delete()
    return redirect('traps')


@login_required
def trap_detail(request, pk):
    trap = Trap.objects.get(id=pk)
    dict = {'trap': trap}
    return render(request, 'classifier/trap/detail.html', dict)


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
    dict = {'form': form, 'trap': trap}
    return render(request, 'classifier/trap/edit.html', dict)

############################
## Functions to Variables ##
############################


@login_required
def variables(request):
    variables = Variable.objects.order_by('id')
    dict = {'variables': variables}
    return render(request, 'classifier/variable/main.html', dict)


@login_required
def variable_new(request):
    if request.method == "POST":
        form = VariableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('variables')
    else:
        form = VariableForm()

    dict = {'form': form}
    return render(request, 'classifier/variable/new.html', dict)


@login_required
def variable_delete(request, pk):
    variable = Variable.objects.get(id=pk)
    variable.delete()
    return redirect('variables')


@login_required
def variable_detail(request, pk):
    variable = Variable.objects.get(id=pk)
    dict = {'variable': variable}
    return render(request, 'classifier/variable/detail.html', dict)


@login_required
def variable_edit(request, pk):
    variable = Variable.objects.get(id=pk)

    if request.method == "POST":
        form = TrapForm(request.POST, instance=variable)
        if form.is_valid():
            form.save()
            return redirect('variables')
    else:
        form = TrapForm(instance=variable)
    dict = {'form': form, 'variable': variable}
    return render(request, 'classifier/variable/edit.html', dict)

#######################
## Functions to Data ##
#######################


@login_required
def view_data(request):
    data = Trap_Image_Data.objects.order_by('id')[:20]
    dict = {'data': data}
    return render(request, 'classifier/data/main.html', dict)


@login_required
def data_new(request):
    images = Trap_Image.objects.order_by('id')
    variables = Variable.objects.order_by('id')
    insects = Insect.objects.order_by('id')

    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data')
    else:
        form = DataForm()

    dict = {'form': form, 'images': images,
            'variables': variables, 'insects': insects}
    return render(request, 'classifier/data/new.html', dict)


@login_required
def data_delete(request, pk):
    data = Trap_Image_Data.objects.get(id=pk)
    data.delete()
    return redirect('data')


@login_required
def data_detail(request, pk):
    data = Trap_Image_Data.objects.get(id=pk)
    dict = {'data': data}
    return render(request, 'classifier/data/detail.html', dict)


@login_required
def data_edit(request, pk):
    data = Trap_Image_Data.objects.get(id=pk)
    images = Trap_Image.objects.order_by('id')
    variables = Variable.objects.order_by('id')
    insects = Insect.objects.order_by('id')

    if request.method == "POST":
        form = DataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('data')
    else:
        form = DataForm(instance=data)
    dict = {'form': form, 'data': data, 'images': images,
            'variables': variables, 'insects': insects}
    return render(request, 'classifier/data/edit.html', dict)
