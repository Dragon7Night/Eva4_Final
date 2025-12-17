from django.contrib import admin


from reservaApp.models import Estado, Reserva



# CRUD del administrador para Cargo 
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['id','estado']

admin.site.register(Estado, EstadoAdmin)


# CRUD del administrador para el Empleado
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_persona','telefono','fecha','hora','cant_personas','observacion','estado']

admin.site.register(Reserva, ReservaAdmin)



