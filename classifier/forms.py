from django import forms

from backend.models import Insect, Trap, Trap_Image, Trap_Image_Data


class ImageForm(forms.ModelForm):
    class Meta:
        model = Trap_Image
        fields = ['trap', 'image', ]
        widgets = {
            'image': forms.TextInput(attrs={'type': 'hidden'}),
        }


class InsectForm(forms.ModelForm):
    class Meta:
        model = Insect
        fields = ['description', ]


class TrapForm(forms.ModelForm):
    class Meta:
        model = Trap
        fields = ['description', ]


class DataForm(forms.ModelForm):
    class Meta:
        model = Trap_Image_Data
        fields = ['image', 'insect', 'value', 'x', 'y', ]
