from django.shortcuts import render, redirect
from ..models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm, BusquedaForm

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'miapp/agregar_categoria.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'miapp/agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'miapp/agregar_cliente.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino_busqueda']
            resultados = Producto.objects.filter(nombre__icontains=termino)
            return render(request, 'miapp/resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'miapp/buscar.html', {'form': form})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'miapp/lista_categorias.html', {'categorias': categorias})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'miapp/lista_productos.html', {'productos': productos})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'miapp/lista_clientes.html', {'clientes': clientes})
