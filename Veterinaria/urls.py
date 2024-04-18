from django.urls import path
from .views import DuenosViewSet, MascotasViewSet, CitasViewSet

urlpatterns = [
    #urls duenos
    path('duenos/', DuenosViewSet.as_view({'get': 'list', 'post': 'create'}), name='duenos'),
    path('duenos/<int:pk>', DuenosViewSet.as_view({'get': 'retrieve','put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='dueno_detalles'),

    #urls mascotas
    path('mascotas/', MascotasViewSet.as_view({'get': 'list', 'post': 'create'}), name='mascotas'),
    path('mascotas/<int:pk>', MascotasViewSet.as_view({'get': 'retrieve','put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='mascota_detalles'),

    #urls mascotas
    path('citas/', CitasViewSet.as_view({'get': 'list', 'post': 'create'}), name='citas'),
    path('citas/<int:pk>', CitasViewSet.as_view({'get': 'retrieve','put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='cita_detalles'),
]