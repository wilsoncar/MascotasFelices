from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Duenos, Mascotas, Citas, Desparasitaciones
from .serializers import DuenosSerializer, MascotasSerializer, CitasSerializer, DesparasitacionesSerializer
from rest_framework.response import Response

# Create your views here.

class DuenosViewSet(viewsets.ModelViewSet):
    queryset = Duenos.objects.all()
    serializer_class = DuenosSerializer

    def list(self, request, *args, **kwargs):
        queryset = Duenos.objects.all().filter(status="Active")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response_data = {
            "message": "Dueño creado",
            "Dueño": serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
    

class MascotasViewSet(viewsets.ModelViewSet):
    queryset = Mascotas.objects.all()
    serializer_class = MascotasSerializer

    def list(self, request, *args, **kwargs):
        queryset = Mascotas.objects.all().filter(status="Active")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response_data = {
            "message": "Mascota creada",
            "Mascota": serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
    

class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer

    def list(self, request, *args, **kwargs):
        queryset = Citas.objects.all().filter(status="Done")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response_data = {
            "message": "Cita creada",
            "Cita": serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
    

class DesparasitacionesViewSet(viewsets.ModelViewSet):
    queryset = Desparasitaciones.objects.all()
    serializer_class = DesparasitacionesSerializer

    def list(self, request, *args, **kwargs):
        queryset = Desparasitaciones.objects.all().filter(status="Completado")
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        response_data = {
            "message": "Desparasitación creada",
            "Desparasitación": serializer.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
    
