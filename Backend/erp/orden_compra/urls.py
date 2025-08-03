from django.urls import path
from . import views

app_name = 'orden_compra'

urlpatterns = [
    path('proveedores_lista', views.ProveedorLista.as_view(), name='proveedor_lista'),
    path('proveedore_nuevo', views.ProveedorNuevo.as_view(), name='proveedor_nuevo'),
    path('proveedor_actualizar', views.ProveedorActualizar.as_view(), name='proveedor_actualizar'),
    path('proveedor_eliminar', views.ProveedorEliminar.as_view(), name='proveedor_eliminar'),
    path('producto_lista', views.ProductoLista.as_view(), name='proveedor_lista'),
    path('producto_nuevo', views.ProductoNuevo.as_view(), name='proveedor_nuevo'),
    path('producto_actualizar', views.ProductoActualizar.as_view(), name='proveedor_actualizar'),
    path('producto_eliminar', views.ProductoEliminar.as_view(), name='proveedor_eliminar'),
    # path('nueva'), views.orden_compra_nueva, name='nueva_orden'
]