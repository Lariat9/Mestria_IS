from django import forms 
from datetime import date

from .models import Proveedor, Producto, Orden_compra, Inventario, Detalle_Orden_Compra

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del proveedor'}),
            'email':forms.EmailField(attrs={'class':'form-control'}),
            'rfc':forms.EmailField(attrs={'class':'form-control'})
        }

        labels = {
            'nombre': 'Nombre del proveedor',
            'email': 'Correo del proveedor',
            'rfc': 'Clave de registro federal de contribuyentes'
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Producto'}),
            'precio': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio del producto'}),
            'proveedor': forms.Select(attrs={'class':'select2'}),
        }
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'proveedor': 'Proveedores'
        }

class OrdenCompraform(forms.ModelForm):
    class Meta:
        model = Orden_compra
        fields = '__all__'
        widgets = {
            'fecha_orden': forms.DateField(attrs={'type': 'date'}),
            'fecha_recepcion': forms.DateField(attrs={'type': 'date'}),
            'proveedor': forms.Select(attrs={'class':'select2'}),
        }
        labels = {
            'fecha_orden': 'Fecha en la que se realizo la orden',
            'fecha_recepcion': 'Fecha de recepcion de la orden',
            'proveedor': 'Proveedores',
        }

class OrdenCompraActualizarform(forms.ModelForm):
    class Meta:
        model = Orden_compra
        fields = 'fecha_recepcion, proveedor'
        widgets = {
            'fecha_recepcion': forms.DateField(attrs={'type': 'date'}),
            'proveedor': forms.Select(attrs={'class':'select2'}),
        }
        labels = {
            'fecha_recepcion': 'Fecha de recepcion de la orden',
            'proveedor': 'Proveedores',
        }

class DetalleOrdenCompraForm(forms.ModelForm):
    class Meta:
        model: Detalle_Orden_Compra
        fields = "cantidad,producto"
        widgets = {
            'cantidad': forms.IntegerField(attrs={'class':'form-control', 'placeholder':'Cantidad por producto'}),
            'producto': forms.Select(attrs={'class':'select2'}),
        }
        labels = {
            'cantidad': 'Cantidad de producto ordenado',
            'producto': 'Lista de productos',
        }

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = '__all__'
        widgets = {
            'ubicacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Producto'}),
            'cantidad': forms.IntegerField(attrs={'class':'form-control', 'placeholder':'Cantidad por producto'}),
            'productos': forms.Select(attrs={'class':'select2'}),
        }

        labels = {
            'ubicacion': 'Lugar en el que se almacena el producto',
            'cantidad': 'Cantidad por producto disponible',
            'productos': 'Seleccion de producto'
        }