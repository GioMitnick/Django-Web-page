from django.db import models


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300)
    precio = models.FloatField()
    cantidad = models.IntegerField(default=0)
