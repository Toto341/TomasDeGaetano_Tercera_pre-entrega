from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request,'AppCoder/inicio.html')

def clientes(request):
    return render(request, 'AppCoder/clientes.html')

def productos(request):
    return render(request,'AppCoder/productos.html')

def marcas(request):
    return render(request,'AppCoder/marcas.html')



print("Hola")