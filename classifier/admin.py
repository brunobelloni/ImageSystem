from django.contrib import admin

from .models import Insect, Trap, Trap_Image, Trap_Image_Data, Variable


class Data(admin.ModelAdmin):
    list_display = ('id', 'image', 'variable', 'insect', 'value', 'x', 'y')
    search_fields = ('id',)


admin.site.register(Trap)
admin.site.register(Insect)
admin.site.register(Variable)
admin.site.register(Trap_Image)
admin.site.register(Trap_Image_Data, Data)
