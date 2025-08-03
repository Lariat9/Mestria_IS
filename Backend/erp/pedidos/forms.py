from django import forms

from .models import Cliente, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        Model = Cliente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del proveedor'}) ,
            'email': forms.EmailField(attrs={'class':'form-control'}),
            'telefono': forms.IntegerField(attrs={'class':'form-control'}),
            'rfc': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del proveedor'})
        }
        labels = {
            'nombre': 'Nombre del cliente',
            'email': 'Correo del cliente',
            'rfc': 'Clave de registro federal de contribuyentes'
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        Model=Pedido
        fields = '__all__'
        widgets={
            'fecha_pedido' : forms.DateField(attrs={'type': 'date'}),
            'cliente': forms.Select(attrs={'class':'select2'}),
        }
        labels = {
            'fecha_pedido' : 'Fecha en la que el cliente hace el pedido',
            'cliente': 'Cliente que solicita el pedido',
        }

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        Model=Pedido
        fields = 'cantidad, producto'
        widgets={
            'cantidad': forms.IntegerField(attrs={'class':'form-control'}),
            'producto': forms.Select(attrs={'class':'select2'})
        }
        labels = {
            'cantidad': 'Cantidad de producto solicitado',
            'producto': 'Producto solicitado'
        }