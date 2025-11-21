from django.shortcuts import render
from .models import habitacion
from .serializers import habitacionserializer
from rest_framework import generics


class habitacionleercrear(generics.ListCreateAPIView):
    queryset = habitacion.objects.all()
    serializer_class = habitacionserializer

class habitacioneliminarmodificar(generics.RetrieveUpdateDestroyAPIView):
    queryset = habitacion.objects.all()
    serializer_class = habitacionserializer 

# Create your views here.
