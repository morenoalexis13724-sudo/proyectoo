from django.shortcuts import render
from .models import reserva
from .serealizers import reservaserializer
from rest_framework import generics


class reservaleercrear(generics.ListCreateAPIView):
    queryset = reserva.objects.all()
    serializer_class = reservaserializer

class reservaeliminarmodificar(generics.RetrieveUpdateDestroyAPIView):
    queryset = reserva.objects.all()
    serializer_class = reservaserializer

# Create your views here.
