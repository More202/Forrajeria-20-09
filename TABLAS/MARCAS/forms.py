from django import forms
from .models import *

class Marcaform(forms.ModelForm):
    class Meta:
        model= Marca
        fields= '__all__'

class Edadform(forms.ModelForm):
    class Meta:
        model= Edad
        fields= '__all__'

class Empleadoform(forms.ModelForm):
    class Meta:
        model= Empleado
        fields= '__all__'

class Categoriaform(forms.ModelForm):
    class Meta:
        model= Categoria
        fields= '__all__'

class Sucursalform(forms.ModelForm):
    class Meta:
        model= Sucursal
        fields= '__all__'

class Clienteform(forms.ModelForm):
    class Meta:
        model= Cliente
        fields= '__all__'

class Tamañoform(forms.ModelForm):
    class Meta:
        model= Tamaño
        fields= '__all__'

class Animalform(forms.ModelForm):
    class Meta:
        model= Animal
        fields= '__all__'


class Consistenciaform(forms.ModelForm):
    class Meta:
        model= Consistencia
        fields= '__all__'

class Productoform(forms.ModelForm):
    class Meta:
        model= Producto
        fields= '__all__'

class Cajaform(forms.ModelForm):
    class Meta:
        model= Caja
        fields= '__all__'
        widgets = {
            'fecha_hs_ap': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datetime-input'}),
            'fecha_hs_cier': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S', attrs={'class': 'datetime-input'}),
        }
        
class BuscadorProductoForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100, required=False)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

class AperturaCajaForm(forms.Form):
    monto_inicial = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        widget=forms.NumberInput(attrs={'placeholder': 'Monto inicial', 'step': '0.01'})
    )
class Ventaform(forms.ModelForm):
    class Meta:
        model= Venta
        fields= '__all__'

class DetalleVentaform(forms.ModelForm):
    class Meta:
        model= DetalleVenta
        fields= '__all__'


        