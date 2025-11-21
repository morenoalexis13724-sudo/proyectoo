from rest_framework import serializers
from .models import servicioreserva


class servicioreservaserializer(serializers.ModelSerializer):

    class Meta:
        model = servicioreserva
        fields = ['servicio','telefono',' salida','email']