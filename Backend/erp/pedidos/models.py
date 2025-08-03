from django.db import models
from django.core.validators import RegexValidator
from orden_compra.models import Producto

class Cliente(models.Model):
    """
        Args:
            - nombre(str): Nombre del cliiente
            - email(email): Correo del cliente
            - telefono(int): Telefono del cliente
            - RFC(str): Clave de Registro Federal de Contribuyentes
    """
    nombre = models.CharField(
        verbose_name="Nombre del cleinte", max_length=100, blank=False, null=False)
    email = models.EmailField(verbose_name="E-mail del cliente", max_length=100, blank=False, null=False)
    telefono = models.IntegerField(verbose_name="Telefono del cliente", blank=False, null=False, validators=[RegexValidator(
        regex='\d{10}',
        message='El numero telefonico no es valido.',
        code='invalid_phone_number')])
    rfc = models.CharField(
        verbose_name="RFC", max_length= 20, validators=[RegexValidator(
        regex='\w{13}',
        message='EL RFC no es válido.',
        code='invalid_name'
    )])

    def __str__(self):
        return self.nombre+ " "+ self.email
    
class Pedido(models.Model):
    """
        Args:
            - folio_pedido
            - fecha_pedido(date): Fecha en la que el cliente solicito el pedido
            - cantidad(int): Cantidad solicitada por producto 
            - cliente(fk): Cliente que solicita un pedido
            - producto(fk): Producto solicictado
    """
    fecha_pedido = models.DateTimeField(
        verbose_name= "Fecha en la que el cliente solicicto el pedido", blank=False, null=False)
    cliente = models.ForeignKey("Cliente", 
                                   verbose_name="Cliente que realizo un pedido",
                                   null = True, blank = True, 
                                    on_delete=models.DO_NOTHING)
    
    # Definir una llave primaria compuesta
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cliente', 'fecha_pedido'], name='folio_pedido'),
        ] 
    

class DetallePedido(models.Model):
    """
        Args:
            - cantidad(int): Cantidad solicitada por producto 
            - producto(fk): Producto solicictado
            - pedido(fk): Pedido del que forma parte
    """
    cantidad = models.IntegerField(verbose_name= "Cantidad solicictada por producto", blank=False, null=False)
    producto =  models.ForeignKey("orden_compra.Producto", 
                                   verbose_name="Producto solicitado por un cliente",
                                   null = True, blank = True, 
                                    on_delete=models.DO_NOTHING)
    pedido = models.ForeignKey("Pedido", 
                                   verbose_name="Pedido del que forma parte",
                                   null = False, blank = False, 
                                    on_delete=models.CASCADE)
    