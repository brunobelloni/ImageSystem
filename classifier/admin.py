from django.contrib import admin
from .models import (Trap, Trap_Image,
                     Insect, Variable,
                     Trap_Image_Data,)

admin.site.register(Trap)
admin.site.register(Insect)
admin.site.register(Variable)
admin.site.register(Trap_Image)
admin.site.register(Trap_Image_Data)
