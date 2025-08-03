from django.db import models
from django.core.validators import RegexValidator

class Proveedor(models.Model):
    """
        Args:
            - nombre(str): Nombre del proveedor
            - email(email): Correo del proveedor
            - RFC(str): Clave de Registro Federal de Contribuyentes
    """
    nombre = models.CharField(
        verbose_name="Nombre del proveedor", max_length=100, blank=False, null=False)
    email = models.EmailField(verbose_name="E-mail", max_length=100, blank=False, null=False)
    rfc = models.CharField(
        verbose_name="RFC", max_length= 20, validators=[RegexValidator(
        regex='\w{13}',
        message='EL RFC no es válido.',
        code='invalid_name'
    )])

    def __str__(self):
        return self.nombre + " " + self.email
    
class Producto(models.Model):
    """
        Args:
            - nombre(str): Nombre del producto
            - precio(float): Precio del producto
            - proveedor(fk): Relacion a la tabla de proveedores
    """
    nombre = models.CharField(
        verbose_name="Nombre Producto", max_length=150, blank=False, null=False)
    precio = models.FloatField(
        verbose_name="Precio Unitario", blank=False, null=False)
    proveedor = models.ForeignKey("Proveedor", 
                                   verbose_name="Proveedor al que se le solicito un producto",
                                   null = True, blank = True, 
                                    on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.nombre + ": " + self.precio + "$, "+ self.proveedor
    
class Orden_compra(models.Model):
    """
        Args:
            - folio_compra(pk): Folio de la compra de producto
            - fecha_orden(date): Fecha en la que se compro el producto
            - Cantidad(int): Cantidad solicitada por producto y proveedor
            - fecha_recepcion(date): Fecha en la que se recibio el producto solicitado
            - proveedor(fk): Relacion a la tabla de proveedores
            - producto(fk): Relacion a la tabla de productos
    """
    fecha_orden = models.DateTimeField(verbose_name= "Fecha de Orden", blank=False, null=False)
    fecha_recepcion = models.DateTimeField(verbose_name= "Fecha de recepcion del producto", blank=True, null=True)
    proveedor = models.ForeignKey("Proveedor", 
                                   verbose_name="Proveedor al que se le solicito un producto",
                                   null = True, blank = True, 
                                    on_delete=models.DO_NOTHING)
    
    
    # Definir una llave primaria compuesta
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['proveedor', 'fecha_orden'], name='folio_compra'),
        ] 
class Detalle_Orden_Compra(models.Model):
    """
        Args:
            - Cantidad(int): Cantidad solicitada por producto y proveedor
            - producto(fk): Relacion a la tabla de productos
            - orden_compra(fk): Orden a la que pertenece este detalle de compra
    """
    cantidad = models.IntegerField(verbose_name= "Cantidad comprada de un producto", blank=False, null=False)
    producto =  models.ForeignKey("Producto", 
                                   verbose_name="Producto solicitado a un proveedor",
                                   null = True, blank = True, 
                                    on_delete=models.DO_NOTHING)
    orden_compra =  models.ForeignKey("Orden_compra", 
                                   verbose_name="Orden solicitada a un proveedor",
                                   null = True, blank = True, 
                                    on_delete=models.CASCADE)



class Inventario(models.Model):
    """
        Args:
            - ubicacion(str): Ubicacion del producto dentro del almacen
            - cantidad(int): Cantidad disponible del producto 
            - producto(fk): Relacion a la tabla de productos
    """
    ubicacion = models.CharField(verbose_name="Ubicacion del producto dentro del almacen", max_length= 200, blank=True, null=True)
    cantidad = models.IntegerField(verbose_name="Cantidad disponible del producto")
    producto =  models.ForeignKey("Producto", 
                                   verbose_name="Producto disponible en el almacen",
                                   null = True, blank = True, 
                                    on_delete=models.CASCADE)