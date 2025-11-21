from rest_framework import serializers
from .models import habitacion


class habitacionserializer(serializers.ModelSerializer):

    class Meta:
        model = habitacion
        fields = "__all__"