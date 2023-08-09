from django.contrib import admin
from . import models

admin.site.register(models.TipoProducto)

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "categoria",
        "cantidad",
        "precio",
        "fecha_actualizacion"
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre","categoria")
    list_filter = ("nombre",)
    date_hierarchy = "fecha_actualizacion"

@admin.register(models.Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "consulta",
        "fecha_consulta"
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    date_hierarchy = "fecha_consulta"

