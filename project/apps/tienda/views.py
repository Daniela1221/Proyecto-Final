from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from . import models, forms

def home(request):
    return render(request,"tienda/index.html")

def carrito(request):
    return render(request,"tienda/carrito.html")

def contacto(request):
    if request.method == "POST":
        form = forms.ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            contexto = {"contacto":"Mensaje enviado, te responderemos vía email a la brevedad."}
            return render(request,"Home/index.html",contexto)
    else:
        form = forms.ContactoForm()
    return render(request,"tienda/contacto.html",{"form":form})

#Productos
class ProductoList(ListView):
    model = models.Producto

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Producto.objects.all()
        return object_list

class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("admin:index")

class ProductoDetail(DetailView):
    model = models.Producto

class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("tienda:producto_list")

class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("tienda:producto_list")