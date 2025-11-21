from rest_framework import serializers
from .models import servicio


class servicioserializer(serializers.ModelSerializer):

    class Meta:
        model = servicio
        fields = ['servicio','telefono',' salida','email']