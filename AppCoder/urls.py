from django.urls import path
from AppCoder import views

urlpatterns = [
    path('',views.inicio, name = "inicio"),
    path('clientes',views.clientes, name = "clientes"),
    path('productos',views.productos, name = "productos"),
    path('marcas',views.marcas, name = "marcas"),
]
