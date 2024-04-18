from django.contrib import admin
from .models import Duenos, Mascotas, Citas, Desparasitaciones

# Register your models here.
admin.site.register(Duenos, list_display=['id_dueno', 'nombre', 'direccion', 'telefono','correo', 'status'])
admin.site.register(Mascotas, list_display=['id_mascota', 'id_dueno', 'nombre', 'sexo', 'raza', 'edad', 'status'])
admin.site.register(Citas, list_display=['id_cita', 'id_mascota', 'fecha', 'hora', 'tipo_cita', 'status'])
admin.site.register(Desparasitaciones, list_display=['id_desparasitacion', 'id_mascota', 'tipo', 'fecha', 'status'])

