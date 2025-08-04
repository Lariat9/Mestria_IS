from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import * 
from .forms import *

class ProveedorLista(ListView):
    model = Proveedor
    template_name= "Proveedor_lista.html"

class ProveedorNuevo(CreateView):
    model = Proveedor
    template_name = "Proveedor_nuevo.html"

class ProveedorActualizar(UpdateView):
    model = Proveedor
    template_name = "Proveedor_actualizar.html"

class ProveedorEliminar(DeleteView):
    model = Proveedor
    template_name = "Proveedor_actualizar.html"

class ProductoLista(ListView):
    model = Producto
    template_name = "Producto_lista.html"

class ProductoNuevo(CreateView):
    model = Producto
    template_name = "Producto_nuevo.html"

class ProductoActualizar(UpdateView):
    model = Producto
    template_name = "Producto_actualizar.html"

class ProductoEliminar(DeleteView):
    model = Producto
    template_name  = "Producto_eliminar.html"

class OrdenCompra(ListView):
    model = Orden_compra
    template_name = "Orden_compra_lista.html"

class OrdenCompraNueva(CreateView, LoginRequiredMixin):
    model = Orden_compra, Detalle_Orden_Compra
    template_name = 'Orden_compra_nueva.html'

    def form_valid(self, form):
        form_data = {
            'fecha_orden': self.request.POST.get('fecha_orden'),
            'fecha_recepcion': self.request.POST.get('fecha_recepcion'),
            'proveedor': self.request.POST.get('proveedor'),
        }
        form_compra = OrdenCompraform(data = form_data)
        if form_compra.is_valid():
            orden_compra = form_compra.save()
            orden_compra_folio_compra = orden_compra.folio_compra
            orden_compra = Orden_compra.objects.get(folio_compra = orden_compra_folio_compra)
        
        detalle_orden_compra_arg = []
        for producto in self.request.POST.get('productos'):
            form_data_detalle_compra = {
                'cantidad': producto.cantidad,
                'producto': producto.producto,
                'orden_compra': orden_compra
            }
            form_detalle_compra = DetalleOrdenCompraForm(data = form_data_detalle_compra)
            if form_detalle_compra.is_valid():
                detalle_orden_compra = form_detalle_compra.save()

        detalle_orden_compra_arg = Detalle_Orden_Compra.objects.get(orden_compra = orden_compra)        
        
        context = {
            'orden_compra': orden_compra,
            'detalle_orden_compra': detalle_orden_compra_arg
        }

        return redirect(reverse_lazy('orden_compra:detalle_compra', context = context))

class OrdenCompraDetalle(DetailView):
    model = Orden_compra
    template_name = 'orden_compra/orden_compra_detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orden_compra = self.get_object()
        detalles_orden_compra = Detalle_Orden_Compra.objects.filter(orden_compra = orden_compra)
        context['orden_compra_form'] = Orden_compra(initial={'orden_compra':orden_compra.folio_compra})
        context['detalles_ordenes_form'] = detalles_orden_compra

        return context
    
class OrdenCompraActualizar(UpdateView,LoginRequiredMixin):
    model = Orden_compra
    form_class = OrdenCompraActualizarform
    template_name = 'orden_compra/orden_compra_actualizar.html'

    def get_context_data(self, **kwargs):
        context = super(). get_context_data(**kwargs)
        orden_compra = Orden_compra.objects.filter(folio_compra = self.object.folio_compra)
        detalles_orden_compra = Detalle_Orden_Compra.objects.filter(orden_compra = orden_compra)
        context['detalles_orden_compra'] = detalles_orden_compra
        return context

    def get_success_url(self):
        return reverse_lazy('orden_compra: orden_compra_detalle', args = [self.object.folio_compra])
    
    def post(self, request, *args, **kwargs):
        orden_compra = self.get_object()
        #Recuperar del post ? (Establecer un id en el front para recuperar )
        detalles_orden_compra = Detalle_Orden_Compra.objects.filter(orden_compra = orden_compra)
        form_detalle_compra = request.POST.copy()

        if form_detalle_compra.is_valid():
            if request.POST.get('fecha_recepcion'):
                for producto in detalles_orden_compra:
                    if Inventario.objects.filter(producto = producto):
                        producto_inventario = Inventario.objects.filter(producto = producto)
                        producto_inventario.cantidad += producto.cantidad
                        producto_inventario.save()
                    else:
                        producto_inventario = Inventario(ubicacion = '', cantidad = producto.cantidad, producto = producto)
                        producto_inventario.save()
        return super(OrdenCompraActualizar, self).post(request, **kwargs)
    
class InventarioActualizar(UpdateView, LoginRequiredMixin):
    model = Inventario
    form_class = InventarioForm
    template_name = 'orden_compra/inventario_actualizar.html'


