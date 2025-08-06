from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import * 
from pedidos.forms import *

class ClienteLista(ListView):
    model = Cliente
    template_name = "cliente/Lista_cliente.html"

class ClienteNuevo(CreateView, LoginRequiredMixin):
    model = Cliente
    template_name = "cliente/Cliente_nuevo.html"

class ClienteActualizar(UpdateView, LoginRequiredMixin):
    model = Cliente
    template_name = "cliente/Cliente_actualizar.html"

class ClienteEliminar(DeleteView, LoginRequiredMixin):
    model = Cliente
    template_name = "CLiente/Cliente_eliminar.html"

class PedidoLista(ListView):
    model = Pedido
    template_name = "Pedido_lista.html"

class PedidoNueva(CreateView, LoginRequiredMixin):
    model = Pedido, DetallePedido
    template_name = 'Pedido_nueva.html'

    def form_valid(self, form):
        form_data = {
            'fecha_pedido': self.request.POST.get('fecha_pedido'),
            'cliente': self.request.POST.get('cliente')
        }

        form_pedido = PedidoForm(data = form_data)
        if form_pedido.is_valid():
            pedido = form_pedido.save()
            pedido_folio = pedido.folio_pedido
            pedido = Pedido.objects.get(folio_pedido = pedido_folio)
        
        detalle_pedido_arg = []
        for d_pedido in self.request.POST.get('pedidos'):
            form_data_detalle_pedido = {
                'cantidad': d_pedido.cantidad,
                'producto': d_pedido.producto,
                'pedido': pedido
            }
            form_detalle_pedido = DetallePedidoForm(data = form_data_detalle_pedido)
            if form_detalle_pedido.is_valid():
                detalle_pedido = form_detalle_pedido.save()

        detalle_pedido_arg = DetallePedido.objects.get(pedido = pedido)

        context = {
            'pedido': pedido,
            'detalle_pedido': detalle_pedido_arg
        }

        return redirect(reverse_lazy('pedido:detalle_pedido', context = context))
    
class PedidoDetalle(DetailView):
    model = Pedido
    template_name = 'pedido/pedido_detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pedido = self.get_object()
        detalles_pedido = DetallePedido.objects.filter(pedido = pedido)
        context['pedido_form'] = Pedido(initial={'pedido': pedido.folio_pedido})
        context['detalles_pedido_form'] = detalles_pedido

        return context
    
class PedidoActualizar(UpdateView, LoginRequiredMixin):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido/pedido_actualizar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pedido = Pedido.objects.filter(folio_pedido = self.object.folio_pedido)
        detalles_pedido = DetallePedido.objects.filter(pedido = pedido)
        context['detalles_pedido'] = detalles_pedido
        return context
    
    def get_success_url(self):
        return reverse_lazy('pedido: pedido_detalle', args = [self.object.folio_pedido])
    
    def post(self, request, *args, **kwargs):
        pedido = self.get_object()
        #Recuperar del post ?
        detalles_pedido= DetallePedido.objects.filter(pedido = pedido)
        form_detalle_pedido = request.POST.copy()

        if form_detalle_pedido.is_valid():
            form_detalle_pedido.save()
            for detalle_p in detalles_pedido:
                detalle_p.save()

        return super(PedidoActualizar, self).post(request, **kwargs) 
        
class PedidoEliminar(DeleteView, LoginRequiredMixin):
    model= Pedido
    template_name='pedidos/pedido_aliminar.html'      