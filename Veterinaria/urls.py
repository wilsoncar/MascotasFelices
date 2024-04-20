from django.urls import path
from .views import DuenosViewSet, MascotasViewSet, CitasViewSet, DesparasitacionesViewSet

urlpatterns = [
    #urls duenos
    path('duenos/', DuenosViewSet.as_view({'get': 'list', 'post': 'create'}), name='duenos'),
    path('duenos/<int:pk>', DuenosViewSet.as_view({'get': 'retrieve','put': 'update', 'patch': 'partial_update'}), name='dueno_detalles'),

    #urls mascotas
    path('mascotas/', MascotasViewSet.as_view({'get': 'list', 'post': 'create'}), name='mascotas'),
    path('mascotas/<int:pk>', MascotasViewSet.as_view({'get': 'retrieve','put': 'update', 'patch': 'partial_update'}), name='mascota_detalles'),

    #urls citas
    path('citas/', CitasViewSet.as_view({'get': 'list', 'post': 'create'}), name='citas'),
    path('citas/<int:pk>', CitasViewSet.as_view({'get': 'retrieve','put': 'update', 'patch': 'partial_update'}), name='cita_detalles'),

    #urls desparasitaciones
    path('desparasitaciones/', DesparasitacionesViewSet.as_view({'get': 'list', 'post': 'create'}), name='desparasitaciones'),
    path('desparasitaciones/<int:pk>', DesparasitacionesViewSet.as_view({'get': 'retrieve','put': 'update', 'patch': 'partial_update'}), name='desparasitaciones_detalles'),
]