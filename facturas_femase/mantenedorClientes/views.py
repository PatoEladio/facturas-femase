from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
            return redirect('dashboard')
    return render(request, "auth/login.html")

@login_required(login_url="/")
def signout(request):
    logout(request)
    return redirect('login')

@login_required
def facturas(request):
    context = {}
    if request.method == "POST":
        form = AddFacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(facturas)
        else:
            context['form'] = form
            return render(request, "adminTemp/facturas.html", context)    
    else:
        obtenerFacturas = Factura.objects.all()
        form = AddFacturaForm()
        context = {
            'form': form,
            'facturas': obtenerFacturas
        }
        return render(request, "adminTemp/facturas.html", context)    

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
    if request.method == "POST":
        form = AddClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Info exitoso")
        else:
            context['form'] = form
            return render(request, "adminTemp/clientes.html", context)    
    else:
        obtenerClientes = Cliente.objects.all().values()
        print(obtenerClientes)
        form = AddClienteForm()
        context = {
            'form': form,
            'clientes': obtenerClientes
        }
        return render(request, "adminTemp/clientes.html", context)    

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
