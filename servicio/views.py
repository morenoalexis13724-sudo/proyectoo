from django.shortcuts import render
from .models import servicio
from .serealizers import servicioserializer
from rest_framework import generics


class servicioleercrear(generics.ListCreateAPIView):
    queryset = servicio.objects.all()
    serializer_class = servicioserializer

class servicioeliminarmodificar(generics.RetrieveUpdateDestroyAPIView):
    queryset = servicio.objects.all()
    serializer_class = servicioserializer

# Create your views here.
