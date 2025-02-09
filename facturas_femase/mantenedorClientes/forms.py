from django import forms
from .models import Cliente, Factura, Servicio


class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
        labels = {
            "rutCliente": "RUT",
            "nombreCliente": "Nombre",
            "nombreContacto1": "Contacto N1",
            "nombreContacto2": "Contacto N2",
            "cargoContacto1": "Cargo contacto N1",
            "cargoContacto2": "Cargo contacto N2",
            "numeroContacto1": "Numero N1",
            "numeroContacto2": "Numero N2",
            "correoContacto1": "Correo N1",
            "correoContacto2": "Correo N2",
        }

    def __init__(self, *args, **kwargs):
        super(AddClienteForm, self).__init__(*args, **kwargs)
        self.fields["nombreContacto2"].required = False
        self.fields["cargoContacto2"].required = False
        self.fields["numeroContacto2"].required = False
        self.fields["correoContacto2"].required = False
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control mt-2"
            field.widget.attrs["autocomplete"] = "off"


class AddFacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = "__all__"
        widgets = {
            "fechaInicio": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
            "fechaFin": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super(AddFacturaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control mt-2"
            field.widget.attrs["autocomplete"] = "off"


class UploadFacturaForm(forms.Form):
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(UploadFacturaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control mt-2"
            field.widget.attrs["autocomplete"] = "off"

class AddServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(AddServicioForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control mt-2"
            field.widget.attrs["autocomplete"] = "off"
