from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import MarcasFormulario, ProductosFormulario,ClientesFormulario
from AppCoder.models import Marcas,Productos,Clientes
def inicio(request):
    return render(request,'AppCoder/inicio.html')

def clientes(request):
    return render(request, 'AppCoder/clientes.html')

def productos(request):
    return render(request,'AppCoder/productos.html')

def marcas(request):
    return render(request,'AppCoder/marcas.html')


def clientesFormulario(request):       

    if request.method == "POST":

        frmClientes = ClientesFormulario(request.POST)

        if frmClientes.is_valid():

            data = frmClientes.cleaned_data

            nombre = data.get('nombre')
            apellido = data.get('apellido')
            dni = data.get('dni')
            email = data.get('email')

            clientes = Clientes(nombre = nombre,
                                apellido = apellido,
                                dni = dni,
                                email = email,
                                )
            clientes.save()

            return render(request, "AppCoder/inicio.html")      

    else:

        frmClientes = ClientesFormulario()
    
    return render(request, "AppCoder/clientesFormulario.html", {"frmClientes":frmClientes})



def productosFormulario(request):       

    if request.method == "POST":

        frmProductos = ProductosFormulario(request.POST)

        if frmProductos.is_valid():

            data = frmProductos.cleaned_data

            nombre = data.get('nombre')
            categoria = data.get('categoria')
            precio = data.get('precio')
            stock = data.get('stock')

            productos = Productos(nombre = nombre,
                                  categoria = categoria,
                                  precio = precio,
                                  stock = stock)
            productos.save()

            return render(request, "AppCoder/inicio.html")      

    else:

        frmProductos = ProductosFormulario()
    
    return render(request, "AppCoder/productosFormulario.html", {"frmProductos":frmProductos})


def marcasFormulario(request):       

    if request.method == "POST":

        frmMarcas = MarcasFormulario(request.POST)

        if frmMarcas.is_valid():

            data = frmMarcas.cleaned_data

            marca = Marcas(nombre=data['nombre'])
            marca.save()

            return render(request, "AppCoder/inicio.html")
        
    else:

        frmMarcas = MarcasFormulario()
    
    return render(request, "AppCoder/marcasFormulario.html", {"frmMarcas":frmMarcas})
