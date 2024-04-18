from django.shortcuts import render
from rest_framework import viewsets
from .models import Duenos
from .serializers import DuenosSerializer
from rest_framework.response import Response

# Create your views here.

class DuenosViewSet(viewsets.ModelViewSet):
    queryset = Duenos.objects.all()
    serializer_class = DuenosSerializer
    permission_classes = []

    #def list(self, request, *args, **kwargs):
        #queryset = Duenos.objects.all().filter(status='Active')
        #serializer = self.get_serializer(queryset, many='Active')
        #return Response(serializer.data)
