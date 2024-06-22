# Productos/models.py

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300)
    precio = models.FloatField()
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
