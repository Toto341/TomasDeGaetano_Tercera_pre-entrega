from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import MarcasFormulario, ProductosFormulario,ClientesFormulario
from AppCoder.models import Marcas,Productos,Clientes
def inicio(request):
    return render(request,'AppCoder/inicio.html')

def clientes(request):
     
     clientes = Clientes.objects.all()

     return render(request, 'AppCoder/clientes.html', {"clientes":clientes})

def productos(request):
     
     productos = Productos.objects.all()
     return render(request,'AppCoder/productos.html', {"productos":productos})

def marcas(request):

    marcas = Marcas.objects.all()
    return render(request,'AppCoder/marcas.html',{"marcas":marcas})


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
                                  stock = stock,)
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

def formBuscarProducto(request):

    return render(request, 'AppCoder/busquedaProducto.html')


def buscarProducto(request):

    if request.method == "GET":

        nombre = request.GET.get("producto")
       
        if nombre is None:
            
            return HttpResponse("Debe completar el campo producto")
        
        else:

            productos = Productos.objects.filter(nombre__icontains=nombre)
            return render(request, "AppCoder/resultadosBuscarProductos.html", {"productos":productos})
        

def eliminar_producto(request,id_producto):

    producto = Productos.objects.get(id=id_producto)

    producto.delete()

    #Vuelve al menu

    productos = Productos.objects.all() #Trae todos los productos

    return render(request, "AppCoder/productos.html", {"productos":productos}) # renderiza el template productos.html y le pasa el contexto 

    
