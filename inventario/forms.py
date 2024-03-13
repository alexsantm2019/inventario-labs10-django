#aqui crearemos nuestros formularios,los cuales me van a permitir hacer la carga, mucho mas eficiente y rapida
#* Ventaja: evitamos tener que agregar campo por campo, cada detalle que estemos precisando
#* desventaja: no presentan ningun tipo de estilo, por lo cual, debemos nosotros, a traves de CSS, darle un diseño

#desde Django, debemos traernos el metodo, junto la clase de Formularios

from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):   
    class Meta:
        model = Productos
        fields = ['nombre_producto','precio_producto','stock_producto','categoria_fk', 'origen_producto', 'imagen_producto']


    def clean_imagen_producto(self):
        # Obtenemos la imagen enviada en el formulario
        nueva_imagen = self.cleaned_data.get('imagen_producto')

        # Si estamos editando y hay una imagen nueva, la asignamos al campo
        if nueva_imagen and self.instance.id:
            self.instance.imagen_producto = nueva_imagen

        return nueva_imagen