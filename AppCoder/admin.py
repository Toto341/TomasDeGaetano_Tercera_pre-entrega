from django.contrib import admin
from .models import * 

#Se registra los modelos

admin.site.register(Clientes)

admin.site.register(Productos)

admin.site.register(Marcas)

#User: toto
#password: Sat261109