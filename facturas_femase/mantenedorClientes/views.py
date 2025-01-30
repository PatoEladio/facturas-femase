from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

from .forms import AddClienteForm, AddFacturaForm, UploadFacturaForm
from .models import Cliente, Factura, FacturaImportada

import pandas as pd
import numpy as np


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(
                request, "auth/login.html", {"error": "Credenciales incorrectas!"}
            )
        else:
            login(request, user)
            return redirect("facturas")
    return render(request, "auth/login.html")


@login_required(login_url="/")
def signout(request):
    logout(request)
    return redirect("login")


@login_required(login_url="/")
def facturas(request):
    context = {}
    obtenerFacturas = Factura.objects.all()
    obtenerClientes = Cliente.objects.all()
    if request.method == "GET":
        form = AddFacturaForm()
        context = {
            "form": form,
            "facturas": obtenerFacturas,
            "clientes": obtenerClientes,
        }
        return render(request, "adminTemp/facturas.html", context)
    else:
        try:
            form = AddFacturaForm(request.POST)
            form.save()
            return redirect("facturas")
        except:
            return render(
                request,
                "adminTemp/facturas.html",
                {"form": form, "error": True, "facturas": obtenerFacturas},
            )


@login_required(login_url="/")
def cambiarEstadoFactura(request, factura_id):
    if request.method == "POST":
        factura = get_object_or_404(Factura, pk=factura_id)
        if factura.estado == "LISTO":
            factura.estado = "PENDIENTE"
        elif factura.estado == "PENDIENTE":
            factura.estado = "LISTO"

        factura.save()
        return redirect("facturas")


@login_required(login_url="/")
def subirFactura(request):
    if request.method == "GET":
        form = UploadFacturaForm()
        return render(request, "adminTemp/subirFactura.html", {"form": form})
    else:
        try:
            form = UploadFacturaForm(request.POST, request.FILES)
            if form.is_valid():
                dataframe = pd.read_excel(request.FILES["file"])
                print(dataframe)
                df = dataframe.drop("Cargos", axis=1)
                df = df.dropna()
                for index, dato in df.iterrows():
                    FacturaImportada.objects.bulk_create(
                        [
                            FacturaImportada(
                                dato["N° Doc."], dato["Descripción"], dato["Abonos"]
                            )
                        ]
                    )
                return redirect("importadas")
        except IntegrityError:
            return render(
                request, "adminTemp/subirFactura.html", {"form": form, "error": True}
            )


@login_required(login_url="/")
def facturasImportadas(request):
    importadas = FacturaImportada.objects.values().all()
    facturas = Factura.objects.values().all()
    
    data = [{"importadas": importadas, "filtro": facturas}]

    return render(request, "adminTemp/facturaImportada.html", {"datos": data})

@login_required(login_url="/")
def aprobarRechazarFactura(request, abono):
    factura = Factura.objects.filter(monto=abono).values()
    print(factura)
    return render(request, 'adminTemp/aprobarFacturas.html', {'factura': factura})


@login_required(login_url="/")
def eliminarFactura(request, factura_id):
    factura = get_object_or_404(Factura, pk=factura_id)
    if request.method == "POST":
        factura.delete()
        return redirect("facturas")


@login_required(login_url="/")
def actualizarFactura(request, factura_id):
    if request.method == "GET":
        factura = get_object_or_404(Factura, pk=factura_id)
        form = AddFacturaForm(instance=factura)
        return render(
            request,
            "adminTemp/actualizarFactura.html",
            {"factura": factura, "form": form},
        )
    else:
        factura = get_object_or_404(Factura, pk=factura_id)
        form = AddFacturaForm(request.POST, instance=factura)
        form.save()
        return redirect("facturas")


@login_required(login_url="/")
def clientes(request):
    context = {}
    obtenerClientes = Cliente.objects.all().values()
    if request.method == "GET":
        form = AddClienteForm()
        context = {"form": form, "clientes": obtenerClientes}
        return render(request, "adminTemp/clientes.html", context)
    else:
        try:
            form = AddClienteForm(request.POST)
            form.save()
            return redirect("clientes")
        except:
            return render(
                request,
                "adminTemp/clientes.html",
                {"form": form, "error": True, "clientes": obtenerClientes},
            )


@login_required(login_url="/")
def actualizarCliente(request, cliente_id):
    if request.method == "GET":
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        form = AddClienteForm(instance=cliente)
        return render(
            request,
            "adminTemp/actualizarCliente.html",
            {"cliente": cliente, "form": form},
        )
    else:
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        form = AddClienteForm(request.POST, instance=cliente)
        form.save()
        return redirect("clientes")


@login_required(login_url="/")
def eliminarCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == "POST":
        cliente.delete()
        return redirect("clientes")
