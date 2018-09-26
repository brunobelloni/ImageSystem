from django import forms

from .models import Insect, Trap, Trap_Image, Trap_Image_Data, Variable


class ImageForm(forms.ModelForm):
    class Meta():
        model = Trap_Image
        fields = ('trap', 'image')


class InsectForm(forms.ModelForm):
    class Meta():
        model = Insect
        fields = ('description',)


class TrapForm(forms.ModelForm):
    class Meta():
        model = Trap
        fields = ('description',)


class VariableForm(forms.ModelForm):
    class Meta():
        model = Variable
        fields = ('description',)


class DataForm(forms.ModelForm):
    class Meta():
        model = Trap_Image_Data
        fields = ('image', 'variable', 'insect', 'value', 'x', 'y',)
