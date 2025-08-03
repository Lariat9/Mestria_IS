from django.urls import path
from . import views

app_name = 'rutas'

urlpatterns = [
    path('conductor_lista', views.ConductorLista.as_view(), 'conductor_lista'),
    path('conductor_nuevo', views.ConductorNuevo.as_view(), 'conductor_nuevo'),
    path('conductor_actualizar', views.ConductorActualizar.as_view(), 'conductor_actualizar'),
    path('conductor_eliminar', views.ConductorActualizar.as_view(), 'conductor_eliminar'),
    path('vehiculo_lista', views.VehiculoLista.as_view(), 'vehiculo_lista'),
    path('vehiculo_nuevo', views.VehiculoNuevo.as_view(), 'vehiculo_nuevo'),
    path('vehiculo_actualizar', views.VehiculoActualizar.as_view(), 'vehiculo_actualizar'),
    path('vehiculo_eliminar', views.VehiculoEliminar.as_view(), 'vehiculo_eliminar'),
    path('ruta_lista', views.RutaLista.as_view(), 'ruta_lista'),
    path('ruta_nueva', views.RutaNueva.as_view(), 'ruta_nueva'),
    path('ruta_actualizar', views.RutaActualizar.as_view(), 'ruta_actualizar'),
    path('ruta_eliminar', views.RutaEliminar.as_view(), 'ruta_eliminar'),
]