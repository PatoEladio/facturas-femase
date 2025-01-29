from django.contrib import admin
from .models import Cliente, Factura, FacturaImportada

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Factura)
admin.site.register(FacturaImportada)
