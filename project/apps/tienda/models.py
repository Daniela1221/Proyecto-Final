from django.db import models
from django.utils import timezone

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre de la Categoría",unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Productos"
        verbose_name_plural = "Categorías de Productos"

class Producto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre",unique=True)
    categoria = models.ForeignKey(TipoProducto,on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    precio = models.PositiveIntegerField(verbose_name="Precio")
    descripcion = models.TextField(max_length=1000,verbose_name="Descrición")
    imagen = models.ImageField(verbose_name="Imagen asociada al producto",upload_to="img_productos",blank=True,null=True)
    fecha_actualizacion = models.DateTimeField(default=timezone.now,editable=False,verbose_name="Fecha de actualización")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Nuevo Producto"
        verbose_name_plural = "Nuevos Productos"

class Contacto(models.Model):
    correo = models.CharField(max_length=100, verbose_name="Correo Suscriptor")
    consulta = models.TextField(max_length=1000)
    fecha_consulta = models.DateTimeField(default=timezone.now,editable=False,verbose_name="Fecha de consulta")

    def __str__(self) -> str:
        return f"{self.correo}"
