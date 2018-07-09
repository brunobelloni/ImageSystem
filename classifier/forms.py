from django import forms
from .models import Trap_Image, Trap, Insect

class ImageForm(forms.ModelForm):
    class Meta():
        model = Trap_Image
        fields = ('trap','image')


class InsectForm(forms.ModelForm):
    class Meta():
        model = Insect
        fields = ('description',)

class TrapForm(forms.ModelForm):
    class Meta():
        model = Trap
        fields = ('description',)
