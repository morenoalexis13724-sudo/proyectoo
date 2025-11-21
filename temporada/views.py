from django.shortcuts import render
from .models import temporada
from .serializers import temporadaserializer
from rest_framework import generics


class temporadaleercrear(generics.ListCreateAPIView):
    queryset = temporada.objects.all()
    serializer_class = temporadaserializer

class temporadaeliminarmodificar(generics.RetrieveUpdateDestroyAPIView):
    queryset = temporada.objects.all()
    serializer_class = temporadaserializer

# Create your views here.
