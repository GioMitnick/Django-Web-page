from django.shortcuts import render
from Productos.models import Producto

# Create your views here.
#def info_productos(request):
#   ps=pr.objects.all()
#  return render (request, 'productos.html',{'Producto':ps})

def index(request):
    pr=Producto.objects.all()
    return render(request, "productos.html", {"Producto":Producto} )