from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .forms import AddClienteForm, AddFacturaForm
from .models import Cliente, Factura

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "auth/login.html", {'error': 'Credenciales incorrectas!'})
        else:
            login(request, user)
            return redirect('facturas')
    return render(request, "auth/login.html")

@login_required(login_url="/")
def signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/")
def facturas(request):
    context = {}
    obtenerFacturas = Factura.objects.all()
    if request.method == 'GET':
        form = AddFacturaForm()
        context = {
            'form': form,
            'facturas': obtenerFacturas
        }
        return render(request, "adminTemp/facturas.html", context)    
    else:
        try:
            form = AddFacturaForm(request.POST)
            form.save()
            return redirect('facturas')
        except:
            return render(request, "adminTemp/facturas.html", { 'form': form, 'error': True, 'facturas': obtenerFacturas})


@login_required(login_url="/")
def eliminarFactura(request, factura_id):
    factura = get_object_or_404(Factura, pk=factura_id)
    if request.method == 'POST':
        factura.delete()
        return redirect('facturas')

@login_required(login_url="/")
def actualizarFactura(request, factura_id):
    if request.method == 'GET':
        factura = get_object_or_404(Factura, pk=factura_id)
        form = AddFacturaForm(instance=factura)
        return render(request, 'adminTemp/actualizarFactura.html', { 'factura': factura, 'form': form })
    else:
        factura = get_object_or_404(Factura, pk=factura_id)
        form = AddFacturaForm(request.POST, instance=factura)
        form.save()
        return redirect('facturas')
    
@login_required(login_url="/")
def clientes(request):
    context = {}
    obtenerClientes = Cliente.objects.all().values()
    if request.method == "GET":
        form = AddClienteForm()
        context = {
            'form': form,
            'clientes': obtenerClientes
        }
        return render(request, "adminTemp/clientes.html", context)
    else:
        try:
            form = AddClienteForm(request.POST)
            form.save()
            return redirect('clientes')
        except:
            return render(request, 'adminTemp/clientes.html', { 'form': form, 'error': True, 'clientes': obtenerClientes})

@login_required(login_url="/")   
def actualizarCliente(request, cliente_id):
    if request.method == 'GET':
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        form = AddClienteForm(instance=cliente)
        return render(request, 'adminTemp/actualizarCliente.html', {'cliente': cliente, 'form': form})
    else:
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        form = AddClienteForm(request.POST, instance=cliente)
        form.save()
        return redirect('clientes')

@login_required(login_url="/")
def eliminarCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
