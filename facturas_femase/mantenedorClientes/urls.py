from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("facturas/", views.facturas, name="facturas"),
    path(
        "facturas/<int:factura_id>/eliminar",
        views.eliminarFactura,
        name="eliminarFactura",
    ),
    path(
        "facturas/<int:factura_id>/actualizar",
        views.actualizarFactura,
        name="actualizarFactura",
    ),
    path("clientes/", views.clientes, name="clientes"),
    path(
        "clientes/<int:cliente_id>/eliminar",
        views.eliminarCliente,
        name="eliminarCliente",
    ),
    path(
        "actualizarCliente/<int:cliente_id>",
        views.actualizarCliente,
        name="actualizarCliente",
    ),
    path("subirfactura/", views.subirFactura, name='subirFactura'),
    path("cambiarestado/<int:factura_id>", views.cambiarEstadoFactura, name="cambioEstado"),
    path("logout/", views.signout, name="logout"),
]
