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

class ConductorLista(ListView):
    model = Conductor
    template_name = "rutas/Conductor_Lista.html"

class ConductorNuevo(CreateView, LoginRequiredMixin):
    model = Conductor
    template_name = "rutas/Conductor_nuevo.html"

class ConductorActualizar(UpdateView, LoginRequiredMixin):
    model = Conductor
    template_name = "rutas/Conductor_actualizar.html"

class ConductorEliminar(DeleteView, LoginRequiredMixin):
    model = Conductor
    template_name = "rutas/Conductor_eliminar.html"

class VehiculoLista(ListView):
    model = Vehiculo
    template_name = "rutas/Vehiculo_lista.html"

class VehiculoNuevo(CreateView, LoginRequiredMixin):
    model = Vehiculo
    template_name = "rutas/Vehiculo_nuevo.html"

class VehiculoActualizar(UpdateView, LoginRequiredMixin):
    model = Vehiculo
    template_name = "rutas/Vehiculo_actualizar.html"

class VehiculoEliminar(DeleteView, LoginRequiredMixin):
    model = Vehiculo
    template_name = "rutas/Vehiculo_eliminar.html"

class RutaLista(ListView):
    model = Ruta
    template_name = "rutas/Ruta_Lista.html"

class RutaNueva(CreateView, LoginRequiredMixin):
    model = Ruta
    template_name = "rutas/Ruta_nueva.html"

class RutaActualizar(UpdateView, LoginRequiredMixin):
    model = Ruta
    template_name = "rutas/Ruta_actualizar.html"

class RutaEliminar(DeleteView, LoginRequiredMixin):
    model = Ruta
    template_name = "rutas/Ruta_eliminar.html"
    