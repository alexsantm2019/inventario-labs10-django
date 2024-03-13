from typing import Any
from django.db import models

# Create your models here.
''' 

Crear nuestras TABLAS pero basadas en class:
voy a crear una class que represente UNA TABLA y darle los ATRIBUTOS que van a representar los CAMPOS

la tabla se llamara Productos, y tendra los campos nombre_producto , precio_producto, stock_producto.
Esto lo pasara a una class

'''



class Categorias(models.Model):
    nombre_categoria = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nombre_categoria
    
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Productos(models.Model):

    # Definir las opciones para el campo "origen"
    OPCIONES_ORIGEN = (
        ('NAC', 'NACIONAL'),
        ('IMP', 'IMPORTADO'),
    )

    nombre_producto = models.CharField(max_length=30, null=False) # dato: string: restriccion max_length nos dice que el campo no puede tener mas de 30 caracteres, y null=False nos dice que NO PUEDE ESTAR VACIO
    imagen_producto = models.ImageField(upload_to='productos/', null=False, blank=False)
    precio_producto = models.FloatField() # dato: float
    stock_producto = models.IntegerField(default=0) # dato: integer. cuando vayamos a crearlo, si no podemos un stock, automaticamente se completa en 0    
    categoria_fk = models.ForeignKey(Categorias, on_delete=models.CASCADE, null=False)
    origen_producto = models.CharField(max_length=30, null=False, choices=OPCIONES_ORIGEN) # dato: string: restriccion max_length nos dice que el campo no puede tener mas de 30 caracteres, y null=False nos dice que NO PUEDE ESTAR VACIO
    
    def __str__(self) -> str:
        return self.nombre_producto
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'