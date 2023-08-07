from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from . import models

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username","password","email"]
        widgets = {
            "username":forms.TextInput(),
            "password":forms.PasswordInput(),
            "email":forms.TextInput(),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Quita los mensajes de ayuda
        # help_texts = {k: "" for k in fields}
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

class SuscriptorForm(forms.ModelForm):
    class Meta:
        model = models.Suscriptor
        fields = ["nombre","apellido","edad","correo",
                  "nombre_usuario","contraseña","contraseña2"]