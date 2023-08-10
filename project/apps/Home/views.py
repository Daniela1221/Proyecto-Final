from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from . import forms
# Create your views here.

def home(request):
    return render(request, "Home/index.html")

def perfil(request):
    return render(request,"Home/perfil.html")

def login_request(request):
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request,request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            correo = form.cleaned_data.get("email")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, email=correo, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "Home/index.html", {"mensaje":"Inicio de sesión exitoso"})
    else:
        form = forms.CustomAuthenticationForm()
    return render(request,"Home/login.html",{"form":form})

def register(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Home/index.html", {"mensaje": "Suscripción creada con éxito."})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "Home/register.html", {"form": form})

def solicitud(request):
    if request.method == "POST":
        form = forms.TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            contexto = {"solicitud":"La solicitud de empleo fue enviada."}
            return render(request,"Home/index.html",contexto)
    else:
        form = forms.TrabajadorForm()
    return render(request,"Home/solicitud_subscripcion.html",{"form":form})