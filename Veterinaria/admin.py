from django.contrib import admin
from .models import Duenos, Mascotas

# Register your models here.
admin.site.register(Duenos, list_display=['id_dueno', 'nombre', 'direccion', 'telefono','correo', 'status'])
admin.site.register(Mascotas, list_display=['id_dueno', 'id_mascota', 'nombre', 'sexo', 'raza', 'edad', 'status'])

