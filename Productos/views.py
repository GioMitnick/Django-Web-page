# Productos/views.py

from django.shortcuts import render
from .models import Producto

def Productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})
