from django.db import models
from django.utils.translation import gettext_lazy 

class servicioreserva(models.Model):
     
    servicio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    habitacion = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.reserva

# Create your models here.
