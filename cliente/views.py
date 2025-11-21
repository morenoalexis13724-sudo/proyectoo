from django.shortcuts import render
from .models import cliente
from .serializers import clienteserializer
from rest_framework import generics


class clienteleercrear(generics.ListCreateAPIView):
    queryset = cliente.objects.all()
    serializer_class = clienteserializer

class clienteeliminarmodificar(generics.RetrieveUpdateDestroyAPIView):
    queryset = cliente.objects.all()
    serializer_class = clienteserializer    

# Create your views here.
