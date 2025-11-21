from rest_framework import serializers
from .models import cliente

class clienteserializer(serializers.ModelSerializer):

    class Meta:
        model = cliente
        fields = ['nombre','telefono','direccion','email']
