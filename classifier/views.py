from datetime import datetime
from django.shortcuts import render, redirect
from .opencv_library import get_cropped_img, get_data_img
from django.contrib.auth.decorators import login_required
from .models import Trap_Image, Trap, Insect, Variable, Trap_Image_Data
from .forms import ImageForm, InsectForm, TrapForm, VariableForm, DataForm

@login_required
def index(request):
    unclassified_data = Trap_Image_Data.objects.filter(insect=None)
    quantity = len(Trap_Image_Data.objects.filter(insect=None))

    try:
        first = unclassified_data[0]
        b64 = first.image.image
        x, y = first.cordX, first.cordY
        img = get_cropped_img(b64=b64, x=500, y=500, margin=50)
    except Exception as e:
        img = None

    return render(request, 'classifier/index.html', {'unclassified_data': unclassified_data, 'quantity': quantity, 'img': img})


##########################
## Functions to Insects ##
##########################

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


#########################
## Functions to Images ##
#########################

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
def image_new_data(request):
        traps = Trap.objects.all()

        if request.method == "POST":
            form = ImageForm(request.POST)
            if form.is_valid():
                img = form['image'].value()
                id = form.save()
                v_id = Variable.objects.get(id=1)
                x_points, y_points, predict = get_data_img(img)

                for i in range(len(predict)):
                    Trap_Image_Data.objects.create(image=id, variable=v_id, value=predict['area'][i], cordX=x_points[i], cordY=y_points[i])

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

########################
## Functions to Traps ##
########################

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

############################
## Functions to Variables ##
############################

@login_required
def variables(request):
    variables = Variable.objects.all()
    return render(request, 'classifier/variable/main.html', {'variables': variables})

@login_required
def variable_new(request):
    if request.method == "POST":
        form = VariableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('variables')
    else:
        form = VariableForm()

    return render(request, 'classifier/variable/new.html', {'form': form})

@login_required
def variable_delete(request, pk):
    variable = Variable.objects.get(id=pk)
    variable.delete()
    return redirect('variables')

@login_required
def variable_detail(request, pk):
    variable = Variable.objects.get(id=pk)
    return render(request, 'classifier/variable/detail.html', {'variable': variable})

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
    return render(request, 'classifier/variable/edit.html', {'form': form, 'variable': variable})

#######################
## Functions to Data ##
#######################

@login_required
def view_data(request):
    data = Trap_Image_Data.objects.all()
    return render(request, 'classifier/data/main.html', {'data': data})

@login_required
def data_new(request):
    images = Trap_Image.objects.all()
    variables = Variable.objects.all()
    insects = Insect.objects.all()

    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data')
    else:
        form = DataForm()

    return render(request, 'classifier/data/new.html', {'form': form, 'images': images, 'variables': variables, 'insects': insects})

@login_required
def data_delete(request, pk):
    data = Trap_Image_Data.objects.get(id=pk)
    data.delete()
    return redirect('data')

@login_required
def data_detail(request, pk):
    data = Trap_Image_Data.objects.get(id=pk)
    return render(request, 'classifier/data/detail.html', {'data': data})

@login_required
def data_edit(request, pk):
    data = Trap_Image_Data.objects.get(id=pk)

    if request.method == "POST":
        form = DataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('data')
    else:
        form = DataForm(instance=data)
    return render(request, 'classifier/data/edit.html', {'form': form, 'data': data})
