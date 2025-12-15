from django.contrib import admin
from .models import Categoria, Obra, ArquivoObra

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Obra)
admin.site.register(ArquivoObra)    
