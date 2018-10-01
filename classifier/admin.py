from django.contrib import admin

from backend.models import Insect, Trap, Trap_Image, Trap_Image_Data


class Data(admin.ModelAdmin):
    list_display = ('id', 'image', 'insect', 'value', 'x', 'y')
    search_fields = ('id',)


admin.site.register(Trap)
admin.site.register(Insect)
admin.site.register(Trap_Image)
admin.site.register(Trap_Image_Data, Data)
