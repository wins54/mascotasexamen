from django.contrib import admin
from mascotas.models import Mascota, MascotaAdmin, Desempeno, DesempenoAdmin

admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Desempeno, DesempenoAdmin)
