from rest_framework import serializers
from .models import reserva


class reservaserializer(serializers.ModelSerializer):

    class Meta:
        model = reserva
        fields = ['huesped','telefono',' salida','email']