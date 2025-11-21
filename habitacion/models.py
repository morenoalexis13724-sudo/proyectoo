from django.db import models
from django.utils.translation import gettext_lazy 

class habitacion(models.Model):
     
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=15)
    piso = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

# Create your models here.
