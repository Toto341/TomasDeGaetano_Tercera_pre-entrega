from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio',views.inicio, name = "inicio"),
    path('clientes',views.clientes, name = "clientes"),
    path('productos',views.productos, name = "productos"),
    path('marcas',views.marcas, name = "marcas"),

    path('productosFormulario', views.productosFormulario, name="productosFormulario"),
    path('clientesFormulario', views.clientesFormulario, name="clientesFormulario"),
    path('marcasFormulario', views.marcasFormulario, name="marcasFormulario"),

]
