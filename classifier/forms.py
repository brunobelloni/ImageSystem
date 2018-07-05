from django import forms
from .models import Trap_Image, Trap


class ImageForm(forms.ModelForm):
    class Meta:
        model = Trap_Image
        fields = ('image',)
