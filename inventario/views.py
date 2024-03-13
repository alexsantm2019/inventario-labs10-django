from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse
from inventario.models import Productos, Categorias
import os
from django.dispatch import receiver
from django.conf import settings
from .forms import ProductoForm

# Create your views here.
#Creamos LOS CONTROLADORES para administrar nuestra LOGICA, y nuestras VISTAS


def listarProductos(request):
    #deberia devolver EL LISTADO DE LOS PRODUCTOS:
    lista_productos = Productos.objects.all() #Del Modelo Productos, traigo TODOS los objetos
    lista_categorias = Categorias.objects.all()
    opciones_origen = Productos.OPCIONES_ORIGEN  # Obtener las opciones de origen del modelo Producto    
    formulario = ProductoForm()
    #crearemos un CONTEXTO: un diccionario que mediante UNA LLAVE (que sera la que se mostrara y usara en el HTML) y un valor (pondremos LO QUE QUERRAMOS ENVIARLE) nos permitira ENIVAR Y RENDERIZAR DATOS    
    contexto = {'productos': lista_productos, 'categorias': lista_categorias, 'opciones_origen': opciones_origen,'formulario':formulario}

    return render(request,'listado.html', context=contexto)

# def crearProductoOld(request):
#     #capturo LOS name que provienen de los input, desde la request
#     nombre = request.POST['nombre'].capitalize()
#     precio = request.POST['precio']
#     stock = request.POST['stock']
#     categoria_fk = request.POST['categoria']
#     origen = request.POST['origen']
#     imagen = request.FILES['imagen']

#     #Buscar la CATEGORIA que pertenezca al NUMERO proveniente del POST e INSTANCIARLA
#     categoria = Categorias.objects.get(id=categoria_fk)
    
#     # Guardar la imagen física en la carpeta "media/productos"
#     ruta_imagen = os.path.join('productos', imagen.name)
#     with open(os.path.join(settings.MEDIA_ROOT, ruta_imagen), 'wb') as destino:
#         for chunk in imagen.chunks():
#             destino.write(chunk)  
        
#     #creo mi objeto nuevo de un producto, usando la class Productos
#     producto = Productos(nombre_producto=nombre,precio_producto=precio, stock_producto=stock,categoria_fk=categoria, imagen_producto=ruta_imagen, origen_producto=origen)

#     #debo almacenarlo, usando un metodo
#     producto.save()
#     return redirect('listado')

    
def crearProducto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)  # Agrega request.FILES para manejar archivos adjuntos como imágenes
        if formulario.is_valid():
            formulario.save()
            return redirect('listado')
        else:
            # Si el formulario no es válido, puedes renderizar el formulario nuevamente con los errores
            return render(request, 'listado', {'formulario': formulario})
    else:
        # Si la solicitud no es POST, simplemente renderiza el formulario vacío
        formulario = ProductoForm()

    return render(request, 'listado', {'formulario': formulario})    


# def editarProductoOld(request,id):
#     #buscando el producto para EDITAR
#     #producto_a_editar = Productos.objects.get(id=id)
#     try:
#         producto_a_editar = get_object_or_404(Productos,id=id)
#         lista_categorias = Categorias.objects.all()
#         opciones_origen = Productos.OPCIONES_ORIGEN  # Obtener las opciones de origen del modelo Producto    
#     except Http404:
#         return render(request,'error.html')
    
#     if request.method == 'GET':
#         contexto = {'producto': producto_a_editar, 'categorias': lista_categorias, 'opciones_origen': opciones_origen}
#         return render(request,'edit.html',contexto)
    
#     elif request.method == 'POST':

#         # Verificar si se proporcionó una nueva imagen
#         if 'imagen' in request.FILES:
#             imagen_nuevo = request.FILES['imagen']
#             # Eliminar la imagen anterior si existe
#             if producto_a_editar.imagen_producto:
#                 ruta_imagen_anterior = os.path.join(settings.MEDIA_ROOT, producto_a_editar.imagen_producto.name)
#                 if os.path.exists(ruta_imagen_anterior):
#                     os.remove(ruta_imagen_anterior)
#             # Guardar la nueva imagen
#             ruta_imagen_nueva = os.path.join('productos', imagen_nuevo.name)
#             with open(os.path.join(settings.MEDIA_ROOT, ruta_imagen_nueva), 'wb') as destino:
#                 for chunk in imagen_nuevo.chunks():
#                     destino.write(chunk)
#             producto_a_editar.imagen_producto = ruta_imagen_nueva
#         else:
#             imagen_nuevo = None


#         #capturo los datos
#         nombre_nuevo = request.POST['nombre']
#         precio_nuevo = request.POST['precio']
#         stock_nuevo = request.POST['stock']
#         categoria_id = request.POST['categoria']
#         categoria_nueva = Categorias.objects.get(id=categoria_id)
#         origen_nuevo = request.POST['origen']
#         imagen_nuevo = request.FILES['imagen']

#         #actualizo cada campo del objeto a editar
#         producto_a_editar.nombre_producto = nombre_nuevo
#         producto_a_editar.precio_producto = precio_nuevo
#         producto_a_editar.stock_producto = stock_nuevo
#         producto_a_editar.categoria_fk = categoria_nueva
#         producto_a_editar.origen_producto = origen_nuevo
#         producto_a_editar.categoria_fk = categoria_nueva
#         #ALMACENAMOS LOS CAMBIOS
#         producto_a_editar.save()
#         return redirect('listado')

def editarProducto(request, id):
    producto = get_object_or_404(Productos, id=id)

    if request.method == 'GET':
        formulario = ProductoForm(instance=producto)
        contexto = {'formulario': formulario, 'producto': producto}
        return render(request, 'edit.html', contexto)

    elif request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            # Redirige a la página de detalles del producto o a la lista de productos
            return redirect('listado')
        else:
            # Si el formulario no es válido, puedes renderizar el formulario nuevamente con los errores
            contexto = {'formulario': formulario, 'producto': producto}
            return render(request, 'edit.html', contexto) 
        
    
def eliminarProducto(request,id):
    #buscar cual es el producto que quiero eliminar!
    try:
        producto_a_eliminar = get_object_or_404(Productos,id=id)
    except Http404:
        return render(request,'error.html')
    

# Obtener la ruta de la imagen del producto y eliminarla si existe
    if producto_a_eliminar.imagen_producto:
        if os.path.exists(producto_a_eliminar.imagen_producto.path):
            os.remove(producto_a_eliminar.imagen_producto.path)

    producto_a_eliminar.delete()
    return redirect('listado')

def crearCategoria(request):
    #Capturar el NOMBRE de la CATEGORIA proveniente del POST
    nombre = request.POST['nombre_categoria'].capitalize()
    #Crear un nuevo Objeto desde la clase Categorias
    categoria = Categorias(nombre_categoria=nombre)
    categoria.save()
    return redirect('listado')

