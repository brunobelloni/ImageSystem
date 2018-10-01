from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from backend.models import Insect, Trap, Trap_Image, Trap_Image_Data

from .forms import DataForm, ImageForm, InsectForm, TrapForm


class InsectListView(ListView):
    template_name = "classifier/list.html"
    model = Insect
    context_object_name = "insects"


class InsectCreateView(CreateView):
    template_name = "classifier/create.html"
    model = Insect
    form_class = InsectForm
    success_url = reverse_lazy("classifier:insect_list")


class InsectUpdateView(UpdateView):
    template_name = "classifier/update.html"
    model = Insect
    fields = '__all__'
    context_object_name = 'insect'
    success_url = reverse_lazy("classifier:insect_list")


class InsectDeleteView(DeleteView):
    template_name = "classifier/delete.html"
    model = Insect
    context_object_name = 'insect'
    success_url = reverse_lazy("classifier:insect_list")
