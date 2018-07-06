from django import forms
from .models import Trap_Image, Trap, Insect


class ImageForm(forms.ModelForm):
    class Meta():
        model = Trap_Image
        fields = ('date','trap','image')

        widgets = {
            'date': forms.DateInput(format='%d/%m/%Y'),
        }


class InsectForm(forms.ModelForm):
    class Meta():
        model = Insect
        fields = ('description',)
