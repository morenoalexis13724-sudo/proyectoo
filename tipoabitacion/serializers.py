from rest_framework import serializers
from .models import tipohabitacion


class tipohabitacionserializer(serializers.ModelSerializer):

    class Meta:
        model = tipohabitacion
        fields = ['nombre','telefono','direccion','email']