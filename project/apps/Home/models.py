from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

# Create your models here.

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    edad = models.PositiveIntegerField()
    correo = models.CharField(max_length=100, verbose_name="Correo electrónico")
    nombre_usuario = models.CharField(max_length=50, verbose_name="Nombre de usuario")
    contraseña = models.CharField(max_length=50, verbose_name="Ingrese una contraseña")
    contraseña2 = models.CharField(max_length=50, verbose_name="Confirmar contraseña")
    fecha_solicitud = models.DateTimeField(default=timezone.now,editable=False,verbose_name="Fecha de solicitud")

    class Meta:
        verbose_name = "Suscriptor"
        verbose_name_plural = "Suscriptores"
        ordering = ("-fecha_solicitud",)

    def clean(self):
        if self.contraseña != self.contraseña2:
            raise ValidationError("La contraseña no coincide con la confirmación.")
        elif 18>self.edad:
            raise ValidationError("La persona ingresada no es mayor de edad.")
    

        
        

    