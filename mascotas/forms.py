from django import forms
from .models import Desempeno, Mascota
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import MultiWidget
from django.forms import Widget
from django.forms.widgets import CheckboxSelectMultiple


class DesempenoForm(forms.ModelForm):
    class Meta:
        model = Desempeno
        fields = ('nombre', 'anio', 'mascotas')


def __init__(self, *args, **kwargs):
    super(DesempenoForm, self).__init__(*args, **kwargs)
    self.fields["mascotas"].required = True
    self.fields["mascotas"].help_text = "Ingrese las mascota que despeña un actividad"
    self.fields["mascotas"].queryset = Mascota.objects.all()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    keep_logged = forms.BooleanField(required=False, label="Keep me logged in")


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ('nombre', 'fecha_nacimiento',)
