from django.db import models
from django.utils.translation import gettext_lazy 

class huesped(models.Model):
    
    huesped = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=15)
    capacidad = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return self.nombre

# Create your models here.
