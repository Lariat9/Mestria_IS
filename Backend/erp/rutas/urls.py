from rutas import views
from django.urls import path

app_name = 'rutas'

urlpatterns = [
    path('conductor_lista', views.ConductorLista.as_view(), name='conductor_lista'),
    path('conductor_nuevo', views.ConductorNuevo.as_view(), name='conductor_nuevo'),
    path('conductor_actualizar', views.ConductorActualizar.as_view(), name='conductor_actualizar'),
    path('conductor_eliminar', views.ConductorActualizar.as_view(), name='conductor_eliminar'),
    path('vehiculo_lista', views.VehiculoLista.as_view(), name='vehiculo_lista'),
    path('vehiculo_nuevo', views.VehiculoNuevo.as_view(), name='vehiculo_nuevo'),
    path('vehiculo_actualizar', views.VehiculoActualizar.as_view(), name='vehiculo_actualizar'),
    path('vehiculo_eliminar', views.VehiculoEliminar.as_view(), name='vehiculo_eliminar'),
    path('ruta_lista', views.RutaLista.as_view(), name='ruta_lista'),
    path('ruta_nueva', views.RutaNueva.as_view(), name='ruta_nueva'),
    path('ruta_actualizar', views.RutaActualizar.as_view(), name='ruta_actualizar'),
    path('ruta_eliminar', views.RutaEliminar.as_view(), name='ruta_eliminar'),
]