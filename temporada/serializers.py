from rest_framework import serializers
from .models import temporada


class temporadaserializer(serializers.ModelSerializer):

    class Meta:
        model = temporada
        fields = ['servicio','telefono',' habitacion','email']