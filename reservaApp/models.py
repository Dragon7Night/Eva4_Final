from django.db import models

# Create your models here.


class Estado(models.Model):
    estado = models.CharField(max_length=50)

    def __str__(models):
        return f'{models.estado}'

class Reserva(models.Model):
    nombre_persona = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    cant_personas = models.IntegerField()
    observacion = models.CharField(max_length=300)

    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)


    
    def __str__(models):
        return f'{models.nombre_persona} - {models.telefono} - {models.fecha} - {models.hora} - {models.cant_personas} - {models.observacion} - {models.estado}'
    
