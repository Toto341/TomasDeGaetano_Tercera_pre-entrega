from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    last_name = forms.CharField()
    first_name = forms.CharField()



class Meta:
    model: User
    fields = ["username","email", "password1","password2","last_name" ,"first_name"]




class UserEditForm(forms.Form):

    email = forms.EmailField(label = "ingresar email")
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        
     model: User
     fields = ["username","email", "password1","password2","last_name" ,"first_name"]



