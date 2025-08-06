from pedidos import views
from django.urls import path

app_name = 'pedidos'

urlpatterns = [
    path('cliente_lista', views.ClienteLista.as_view(), name='cliente_lista'),
    path('cliente_nuevo', views.ClienteNuevo.as_view(), name='cliente_nuevo'),
    path('cliente_actualilzar', views.ClienteActualizar.as_view(), name='cliente_actualizar'),
    path('cliente_eliminar', views.ClienteEliminar.as_view(), name='cliente_eliminar'),
    path('pedido_lista', views.PedidoLista.as_view(), name='pedido_lista'),
    path('pedido_nuevo', views.PedidoNueva.as_view(), name='pedido_nuevo'),
    path('pedido_detalle', views.PedidoDetalle.as_view(), name='pedido_detalle'),
    path('pedido_actualizar', views.PedidoActualizar.as_view(), name='pedido_actualizar'),
    path('pedido_eliminar', views.PedidoEliminar.as_view(), name='pedido_eliminar')
]