from django.shortcuts import render
from .models import Producto

# Create your views here.
def info_productos(request):
    ps=pr.objects.all()
    return render (request, 'productos.html',{'Producto':ps})