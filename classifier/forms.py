from django import forms
from .models import Trap_Image, Trap



class ImageForm(forms.ModelForm):

    class Meta:
        model = Trap_Image
        fields = ('trap', 'image',)

        widgets = {
            'trap': forms.ModelChoiceField(to_field_name="name"),
            'image': forms.Textarea(),
        }
