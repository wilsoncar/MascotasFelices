from django.contrib import admin
from .models import Duenos

# Register your models here.
admin.site.register(Duenos, list_display=['id_dueno', 'nombre', 'direccion', 'telefono','correo', 'status'])

