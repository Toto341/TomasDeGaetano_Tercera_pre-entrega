from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
class MarcasFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)

class ProductosFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    categoria = forms.CharField(max_length=40)
    precio = forms.DecimalField(max_digits=6, decimal_places=2)
    stock = forms.IntegerField()    

class ClientesFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    email = forms.EmailField()


