from django.shortcuts import render
from .models import servicioreserva
from .serealizers import servicioreservaserializer
from rest_framework import generics


class servicioreservaleercrear(generics.ListCreateAPIView):
    queryset = servicioreserva.objects.all()
    serializer_class = servicioreservaserializer

class servicioreservaeliminarmodificar(generics.RetrieveUpdateDestroyAPIView):
    queryset = servicioreserva.objects.all()
    serializer_class = servicioreservaserializer
# Create your views here.
