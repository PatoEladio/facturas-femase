from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name='dashboard'),
    path("", views.login_view, name="login"),
    path('clientes/', views.clientes, name="clientes"),
    path('actualizarCliente/<int:cliente_id>', views.actualizarCliente, name='actualizarCliente'),
    path("logout/", views.signout, name='logout')
]