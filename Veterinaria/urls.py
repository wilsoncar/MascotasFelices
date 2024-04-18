from django.urls import path
from .views import DuenosViewSet

urlpatterns = [
    #urls duenos
    path('duenos/', DuenosViewSet.as_view({'get': 'list', 'post': 'create'}), name='duenos'),
    path('duenos/<int:pk>', DuenosViewSet.as_view({'get': 'retrieve','put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='dueno_detalles'),
]