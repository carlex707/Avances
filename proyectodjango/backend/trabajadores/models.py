from django.db import models

class Empleado(models.Model):
    identificador = models.CharField(max_length=3)
    nombre = models.CharField(max_length=35)
    antiguedad = models.CharField(max_length=3)
    proyecto = models.CharField(max_length=35)
    cargo = models.CharField(max_length=35)

    def __str__(self):
        return self.nombre

