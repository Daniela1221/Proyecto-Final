from django import forms
from . import models

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["nombre","categoria","cantidad","precio","descripcion","imagen"]

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = models.TipoProducto
        fields = "__all__"

class ContactoForm(forms.ModelForm):
    class Meta:
        model = models.Contacto
        fields = ["correo","consulta"]
