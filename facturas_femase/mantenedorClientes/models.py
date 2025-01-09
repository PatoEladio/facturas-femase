from django.db import models

class Cliente(models.Model):
    rutCliente = models.CharField(max_length=12)
    nombreCliente = models.CharField(max_length=40)
    nombreContacto1 = models.CharField(max_length=40)
    nombreContacto2 = models.CharField(max_length=40, null=True)
    cargoContacto1 = models.CharField(max_length=20)
    cargoContacto2 = models.CharField(max_length=20, null=True)
    numeroContacto1 = models.IntegerField()
    numeroContacto2 = models.IntegerField(null=True)
    correoContacto1 = models.EmailField()
    correoContacto2 = models.EmailField(null=True)