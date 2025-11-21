from rest_framework import serializers
from .models import huesped


class huespedserializer(serializers.ModelSerializer):

    class Meta:
        model = huesped
        fields = ['huesped','descripcion','capacidad','email']