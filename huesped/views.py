from django.shortcuts import render
from .models import huesped
from .serializers import huespedserializer
from rest_framework import generics


class huespedleercrear(generics.ListCreateAPIView):
    queryset = huesped.objects.all()
    serializer_class = huespedserializer

class huespedeliminarmodificar(generics.RetrieveUpdateDestroyAPIView):
    queryset = huesped.objects.all()
    serializer_class = huespedserializer  

# Create your views here.
