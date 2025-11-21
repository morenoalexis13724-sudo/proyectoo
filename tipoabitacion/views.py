from django.shortcuts import render
from .models import tipohabitacion
from .serializers import tipohabitacionserializer
from rest_framework import generics


class tipohabitacionleercrear(generics.ListCreateAPIView):
    queryset = tipohabitacion.objects.all()
    serializer_class = tipohabitacionserializer

class tipohabitacioneliminarmodificar(generics.RetrieveUpdateDestroyAPIView):
    queryset = tipohabitacion.objects.all()
    serializer_class = tipohabitacionserializer 

# Create your views here.
