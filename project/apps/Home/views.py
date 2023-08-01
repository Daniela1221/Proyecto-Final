from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.urls import reverse
from . import forms
# Create your views here.

def home(request):
    return render(request, "Home/index.html")

def login_request(request):
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request,request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "Home/index.html", {"mensaje":"Inicio de sesión exitoso"})
    else:
        form = forms.CustomAuthenticationForm()
    return render(request,"Home/login.html",{"form":form})
