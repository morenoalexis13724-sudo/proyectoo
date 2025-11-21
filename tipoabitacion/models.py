from django.db import models
from django.utils.translation import gettext_lazy 

class tipohabitacion(models.Model):
     
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

 
    
    


# Create your models here.
