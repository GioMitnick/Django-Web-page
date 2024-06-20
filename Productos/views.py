from django.shortcuts import render

# Create your views here.
def info_productos(request):
    ps=pr.objects.all()
    return render (request, 'productos.html',{'Productos':ps})