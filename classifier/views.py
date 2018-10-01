from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from backend.models import Insect, Trap, Trap_Image, Trap_Image_Data


class InsectListView(ListView):
    template_name = "list.html"
    model = Insect
    context_object_name = "insects"
