#Voy a crear MIS RUTAS de url para ver los datos y tner mis VISTAS para el usuario
from django.urls import path
from inventario.views import listarProductos,crearProducto,editarProducto,eliminarProducto,crearCategoria

urlpatterns = [
    path('', listarProductos,name='listado'),
    path('crear/',crearProducto,name='crear'),
    path('editar/<id>',editarProducto, name='editar'),
    path('eliminar/<id>',eliminarProducto,name='eliminar'),
    path('crear_categoria/',crearCategoria,name='crear_categoria'),
]