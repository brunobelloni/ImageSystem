from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from backend.models import Insect, Trap, Trap_Image, Trap_Image_Data

from .forms import DataForm, ImageForm, InsectForm, TrapForm


class InsectListView(ListView):
    template_name = "classifier/list.html"
    model = Insect
    context_object_name = "insects"

    def get_context_data(self, **kwargs):
        context = super(InsectListView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['length'] = self.model.objects.all().count()
        context['redirect'] = 'classifier:insect_create'
        context['table_name'] = "classifier/tables/insect_table.html"
        return context


class InsectCreateView(CreateView):
    template_name = "classifier/create.html"
    model = Insect
    form_class = InsectForm
    success_url = reverse_lazy("classifier:insect_list")

    def get_context_data(self, **kwargs):
        context = super(InsectCreateView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:insect_list'
        context['form_fields'] = 'classifier/forms/insect_form.html'
        return context


class InsectUpdateView(UpdateView):
    template_name = "classifier/update.html"
    model = Insect
    fields = '__all__'
    context_object_name = 'insect'
    success_url = reverse_lazy("classifier:insect_list")

    def get_context_data(self, **kwargs):
        context = super(InsectUpdateView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:insect_list'
        return context


class InsectDeleteView(DeleteView):
    template_name = "classifier/delete.html"
    model = Insect
    context_object_name = 'insect'
    success_url = reverse_lazy("classifier:insect_list")

    def get_context_data(self, **kwargs):
        context = super(InsectDeleteView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:insect_list'
        return context


class TrapListView(ListView):
    template_name = "classifier/list.html"
    model = Trap
    context_object_name = "traps"

    def get_context_data(self, **kwargs):
        context = super(TrapListView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['length'] = self.model.objects.all().count()
        context['redirect'] = 'classifier:trap_create'
        context['table_name'] = "classifier/tables/trap_table.html"
        return context


class TrapCreateView(CreateView):
    template_name = "classifier/create.html"
    model = Trap
    form_class = TrapForm
    success_url = reverse_lazy("classifier:trap_list")

    def get_context_data(self, **kwargs):
        context = super(TrapCreateView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:trap_list'
        context['form_fields'] = 'classifier/forms/trap_form.html'
        return context


class TrapUpdateView(UpdateView):
    template_name = "classifier/update.html"
    model = Trap
    fields = '__all__'
    context_object_name = 'trap'
    success_url = reverse_lazy("classifier:trap_list")

    def get_context_data(self, **kwargs):
        context = super(TrapUpdateView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:trap_list'
        context['form_fields'] = 'classifier/forms/trap_form.html'
        return context


class TrapDeleteView(DeleteView):
    template_name = "classifier/delete.html"
    model = Trap
    context_object_name = 'trap'
    success_url = reverse_lazy("classifier:trap_list")

    def get_context_data(self, **kwargs):
        context = super(TrapDeleteView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:trap_list'
        return context


class ImageListView(ListView):
    template_name = "classifier/list.html"
    model = Trap_Image
    context_object_name = "images"

    def get_context_data(self, **kwargs):
        context = super(ImageListView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['length'] = self.model.objects.all().count()
        context['redirect'] = 'classifier:image_create'
        context['table_name'] = "classifier/tables/image_table.html"
        return context


class ImageCreateView(CreateView):
    template_name = "classifier/create.html"
    model = Trap_Image
    form_class = ImageForm
    success_url = reverse_lazy("classifier:image_list")

    def get_context_data(self, **kwargs):
        context = super(ImageCreateView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:image_list'
        context['form_fields'] = 'classifier/forms/image_form.html'
        return context


class ImageUpdateView(UpdateView):
    template_name = "classifier/update.html"
    model = Trap_Image
    fields = '__all__'
    context_object_name = 'image'
    success_url = reverse_lazy("classifier:image_list")

    def get_context_data(self, **kwargs):
        context = super(ImageUpdateView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:image_list'
        context['form_fields'] = 'classifier/forms/image_form.html'
        return context


class ImageDeleteView(DeleteView):
    template_name = "classifier/delete.html"
    model = Trap_Image
    context_object_name = 'image'
    success_url = reverse_lazy("classifier:image_list")

    def get_context_data(self, **kwargs):
        context = super(ImageDeleteView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:image_list'
        return context


class DataListView(ListView):
    template_name = "classifier/list.html"
    model = Trap_Image_Data
    context_object_name = "datas"

    def get_context_data(self, **kwargs):
        context = super(DataListView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['length'] = self.model.objects.all().count()
        context['redirect'] = 'classifier:data_create'
        context['table_name'] = "classifier/tables/data_table.html"
        return context


class DataCreateView(CreateView):
    template_name = "classifier/create.html"
    model = Trap_Image_Data
    form_class = DataForm
    success_url = reverse_lazy("classifier:data_list")

    def get_context_data(self, **kwargs):
        context = super(DataCreateView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:data_list'
        context['form_fields'] = 'classifier/forms/data_form.html'
        return context


class DataUpdateView(UpdateView):
    template_name = "classifier/update.html"
    model = Trap_Image
    fields = '__all__'
    context_object_name = 'data'
    success_url = reverse_lazy("classifier:image_list")

    def get_context_data(self, **kwargs):
        context = super(DataUpdateView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:data_list'
        context['form_fields'] = 'classifier/forms/data_form.html'
        return context


class DataDeleteView(DeleteView):
    template_name = "classifier/delete.html"
    model = Trap_Image
    context_object_name = 'data'
    success_url = reverse_lazy("classifier:image_list")

    def get_context_data(self, **kwargs):
        context = super(DataDeleteView, self).get_context_data(**kwargs)
        context['name'] = self.model._meta.verbose_name
        context['redirect'] = 'classifier:data_list'
        return context
