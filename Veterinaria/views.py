from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Duenos, Mascotas
from .serializers import DuenosSerializer, MascotasSerializer
from rest_framework.response import Response

# Create your views here.

class DuenosViewSet(viewsets.ModelViewSet):
    queryset = Duenos.objects.all()
    serializer_class = DuenosSerializer
    permission_classes = []
    

class MascotasViewSet(viewsets.ModelViewSet):
    queryset = Mascotas.objects.all()
    serializer_class = MascotasSerializer
    permission_classes = []
