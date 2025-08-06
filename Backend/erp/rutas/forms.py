from django import forms

from .models import Conductor, Vehiculo, Ruta

class ConoductorForm(forms.ModelForm):
    class Meta:
        Model=Conductor
        fields= '__all__'
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del conductor'}),
            'apellido': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del conductor'}),
            'rfc': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del conductor'})
        }
        labels={
            'nombre': 'Nombre de lconductor',
            'apellido': 'Apelliodos del conductor',
            'rfc': 'Clave de registro federal de contribuyentes'
        }

class VehiculoForm(forms.ModelForm):
    class Meta:
        Model= Vehiculo
        fields = '__all__'
        widgets={
            'placa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'AAA-1111-X'}),
            'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo del vehiculo'})
        }
        labels={
            'placa': 'Placa del vehiculo',
            'modelo': 'Modelo del vhiculo'
        }

class RutaForm(forms.ModelForm):
    class Meta:
        Model= Ruta
        fields = '__all__'
        widgets={
            'fecha_entrega': forms.DateField(),
            'coordenadas': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Poligono de la ruta'}) ,
            'pedido': forms.Select(attrs={'class':'select2'}),
            'conductor': forms.Select(attrs={'class':'select2'}),
            'vehiculo': forms.Select(attrs={'class':'select2'}),
        }
        labels={
            'fecha_entrega': 'Fecha en la que se entrego el pedido',
            'coordenadas': 'Poligono de las coordenadas de la ruta de reparto',
            'pedido': 'Pedio que se va a llevar por esta ruta',
            'conductor': 'Repartidor',
            'vehiculo': 'Vehiculo asignado'
        }