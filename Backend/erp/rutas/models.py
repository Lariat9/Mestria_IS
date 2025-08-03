from django.db import models
from django.core.validators import RegexValidator
from pedidos.models import Pedido

class Conductor(models.Model):
    """
        Args:
            - nombre(str): Nombre del cconductor
            - Apellido(str): Apellido del conductor
            - RFC(str): Clave de Registro Federal de Contribuyentes
    """
    nombre = models.CharField(
        verbose_name="Nombre del conductor", max_length=100, blank=False, null=False)
    Apellido = models.CharField(
        verbose_name="Apellido del conductor", max_length=100, blank=False, null=False)
    rfc = models.CharField(
        verbose_name="RFC", max_length= 20, validators=[RegexValidator(
        regex='\w{13}',
        message='EL RFC no es válido.',
        code='invalid_name'
    )])

class Vehiculo(models.Model):
    """
        Args:
            - modelo(str): Modelo del Vehiculo repartidor
            - Placa(str): Placas de registro del vehiculo
    """
    modelo = models.CharField(verbose_name="Modelo del Vehiculo repartidor", max_length=100, blank=False, null=False)
    placa = models.CharField(
        verbose_name="Modelo del Vehiculo repartidor", max_length=100, validators=[RegexValidator(
        regex='\w{3}-\d{3}-\w{1}|\d{1}',
        message='La matricula es incorrecta.',
        code='invalid_name'
    )])

class Ruta(models.Model):
    """
        Args:
            - fecha_entrega (date): Fecha en la que el pedido fue entregado al cliente
            - coordenas(str): Coordenadas de la ruta de reparto
            - pedido(fk): Pedido a entregar durnate la ruta
            - conductor(fk): Conductor asignado para realizar la ruta de entregas
            - vehiculo(fk): Vehiculo asifgnado para la ruta
    """
    fecha_entrega = models.DateTimeField(verbose_name="Fecha de entrega de pedidos", blank=False, null=False)
    coordenadas = models.CharField(verbose_name="Coordenadas de la ruta de reparto",max_length= 200, blank=False, null=False)
    pedido = models.ForeignKey("pedidos.Pedido", 
                                   verbose_name="Pediod a entregar a traves de esta ruta",
                                   null = True, blank = True, 
                                    on_delete=models.CASCADE)
    conductor = models.ForeignKey("Conductor", 
                                   verbose_name="Conductor asignado a esta ruta de entrega",
                                   null = True, blank = True, 
                                    on_delete=models.DO_NOTHING)
    vehiculo = models.ForeignKey("Vehiculo", 
                                   verbose_name="Vehiculo asignado a esta ruta",
                                   null = True, blank = True, 
                                    on_delete=models.DO_NOTHING)
    # Definir una llave primaria compuesta
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['pedido', 'fecha_entrega'], name='folio_ruta'),
        ] 