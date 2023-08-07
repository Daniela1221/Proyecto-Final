from django.contrib import admin
from . import models

@admin.register(models.Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
    list_display = (
        "nombre","apellido","correo",
        "nombre_usuario","fecha_solicitud",
    )
    list_display_links = ("nombre_usuario",)
    search_fields = ("nombre_usuario","fecha_solicitud")
    list_filter = ("nombre_usuario",)
    date_hierarchy = "fecha_solicitud"