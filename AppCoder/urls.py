from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio',views.inicio, name = "inicio"),
    path('clientes',views.clientes, name = "clientes"),
    path('productos',views.productos, name = "productos"),
    path('marcas',views.marcas, name = "marcas"),

    path('productosFormulario', views.productosFormulario, name="productosFormulario"),
    path('clientesFormulario', views.clientesFormulario, name="clientesFormulario"),
    path('marcasFormulario', views.marcasFormulario, name="marcasFormulario"),

    path('busquedaProducto', views.formBuscarProducto, name="busquedaProducto"),
    path('buscar', views.buscarProducto, name="buscarProducto"),
    
    path('eliminarproducto/<id_producto>', views.eliminar_producto, name="eliminar_producto"),
    path('eliminarmarca/<id_marca>', views.eliminar_marca, name="eliminar_marca"),
    path('login', views.login_request, name="login"),
    path("registrar", views.registrar, name = "registrar"),
    path("logout",LogoutView.as_view(template_name="AppCoder/logout.html"), name='logout'),
    path('editar_perfil', views.editar_perfil, name= "editar_perfil" )
]
