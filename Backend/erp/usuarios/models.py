from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
    
class Usuario(User):
    """
        Args:
            - nombre(str): Nombre del usuario
            - apellidoP (str): Apellido paterno del usuario
            - apellidoM (str): Apellido materno del usuario
            - RFC(str): Clave de Registro Federal de Contribuyentes
            - rol_usuario (fk): Rol del usuario.
    """
    nombre = models.CharField(
        verbose_name="Nombre", max_length=100, blank=False, null=False)
    apellidoP = models.CharField(
        verbose_name="Apellido Paterno", max_length=150, blank=True, null=True)
    apellidoM = models.CharField(
        verbose_name="Apellido Materno", max_length=150, blank=True, null=True)
    rfc = models.CharField(
        verbose_name="RFC", max_length= 150, validators=[RegexValidator(
        regex='\w{13}',
        message='EL RFC no es válido.',
        code='invalid_name'
    )])
    rol_usuario = models.ForeignKey("usuarios.Rol_usuario", 
                                    verbose_name="Rol_usuario", 
                                    null = True, blank = True, 
                                    on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + " " + self.apellidoP
    
class Rol_usuario(models.Model):
    """
        Args:
        - descripcion (str): Título del rol del usuario.
    """
    descripcion =  models.CharField(
        verbose_name="Descripcion Rol", max_length=100, blank=False, null=False)


