from django.contrib import admin
from .models import Imagem, Inseto, Especie, Dado

# Register your models here.

admin.site.register(Imagem)
admin.site.register(Inseto)
admin.site.register(Especie)
admin.site.register(Dado)
