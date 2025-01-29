from django.db import models


class Cliente(models.Model):
    rutCliente = models.CharField(max_length=12, unique=True)
    nombreCliente = models.CharField(max_length=40)
    nombreContacto1 = models.CharField(max_length=40)
    nombreContacto2 = models.CharField(max_length=40, null=True)
    cargoContacto1 = models.CharField(max_length=20)
    cargoContacto2 = models.CharField(max_length=20, null=True)
    numeroContacto1 = models.IntegerField()
    numeroContacto2 = models.IntegerField(null=True)
    correoContacto1 = models.EmailField()
    correoContacto2 = models.EmailField(null=True)

    def __str__(self):
        return self.nombreCliente


estados = (("PENDIENTE", "PENDIENTE"), ("LISTO", "LISTO"))


class Factura(models.Model):
    descripcion = models.CharField(max_length=60)
    codFactura = models.IntegerField(unique=True)
    monto = models.IntegerField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    estado = models.CharField(max_length=20, choices=estados)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class FacturaImportada(models.Model):
    numDocumento = models.CharField(max_length=60, primary_key=True)
    descripcion = models.CharField(max_length=80)
    abonos = models.CharField(max_length=40)