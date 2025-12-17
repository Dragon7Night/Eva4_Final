from django import forms

from django.core import validators
from reservaApp.models import Estado, Reserva


class EstadoForm(forms.Form):
    estado = forms.CharField(
    widget=forms.TextInput(attrs={
        'class':'form-control'
    }),
    label='Estado:')

class EstadoForm(forms.ModelForm):

    class Meta:
        model = Estado
        fields = ['estado']

    estado = forms.CharField(
    widget=forms.TextInput(attrs={
        'class':'form-control'
    }),
    label='Estado:')


class ReservaForm(forms.Form):

    nombre_persona = forms.CharField(validators=[
        validators.MinLengthValidator(1), 
        validators.MaxLengthValidator(60)],
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Nombre de la persona:"
    )

    telefono = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Teléfono:"
    )

    fecha = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        label="Fecha:"
    )

    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
        label="Hora:"
    )

    cant_personas = forms.IntegerField(validators=[
        validators.MinValueValidator(1)
        ],
        widget=forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        label="Cantidad de personas:"
    )

    observacion = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        label="Observación:"
    )

    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), label='Seleccione una de las opciones')


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

    nombre_persona = forms.CharField(validators=[
        validators.MinLengthValidator(1), 
        validators.MaxLengthValidator(60)],
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Nombre de la persona:"
    )

    telefono = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Teléfono:"
    )

    fecha = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        label="Fecha:"
    )

    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
        label="Hora:"
    )

    cant_personas = forms.IntegerField(validators=[
        validators.MinValueValidator(1)
        ],
        widget=forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        label="Cantidad de personas:"
    )

    observacion = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        label="Observación:"
    )

    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), label='Seleccione una de las opciones')



