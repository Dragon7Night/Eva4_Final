from django.shortcuts import render, get_object_or_404

# Importaciones para redireccionamiento
from django.http import HttpResponseRedirect
from django.urls import reverse


# Importaciones de los elementos [Modelos, Formularios y Serializadores]
from reservaApp.models import Estado, Reserva
from reservaApp.forms import EstadoForm, ReservaForm
from reservaApp.serializer import EstadoSerializer, ReservaSerializer


# <-------------REST FRAMEWORK----------------------->

# Importacion de deradores de rest Frameworks
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status


# ------------------------------------------------------------------

# Vista del Home de la pagina visita
def homeGeneral(request):
    return render(request, 'index2.html')

# Vista del Home de la pagina
def homeMain(request):
    return render(request, 'index.html')



# !=================VISTAS CRUD DE DJANGO==========================

# .=========Vista de estado

# Devuelve todos los datos de la tabla Estado
def dataEstado(request):
    estadoObject = Estado.objects.all()
    data = {'EstadoKey':estadoObject}

    return render(request, 'Elementos/Estado/data_estado.html', data)


# Muestra y registra los datos en el formulario de Estado
def registrarEstado(request):
    formEstado = EstadoForm()

    if request.method == 'POST':
        formEstado = EstadoForm(request.POST)
        if formEstado.is_valid():
            formEstado.save()

            return HttpResponseRedirect(reverse('data_estado'))
        
    data = {'formKey':formEstado}
    return render(request, 'Elementos/Estado/crear_estado.html', data)


# Permite editar un estado por ID
def editarEstado(request, id_estado):
    estadoObject = get_object_or_404(Estado, id=id_estado)
    formEstado = EstadoForm(instance=estadoObject)

    if request.method == 'POST':
        formEstado = EstadoForm(request.POST, instance=estadoObject)
        if formEstado.is_valid():
            formEstado.save()
            return HttpResponseRedirect(reverse('data_estado'))
    
    data = {'formKey':formEstado}
    return render(request, 'Elementos/Estado/crear_estado.html', data)


# Permite eliminar un Estado por ID
def eliminarEstado(request, id_estado):
    estadoObject = get_object_or_404(Estado, id=id_estado)
    estadoObject.delete()

    return HttpResponseRedirect(reverse('data_estado'))

# .=========Vista de Reserva

# Devuelve todos los datos de la tabla Reserva
def dataReserva(request):
    reservaObject = Reserva.objects.all()
    data = {'ReservaKey':reservaObject}

    return render(request, 'Elementos/Reserva/data_reserva.html', data)


# Muestra y registra los datos en el formulario de Reserva
def registrarReserva(request):
    formReserva = ReservaForm()

    if request.method == 'POST':
        formReserva = ReservaForm(request.POST)
        if formReserva.is_valid():
            formReserva.save()

            return HttpResponseRedirect(reverse('data_reserva'))
        
    data = {'formKey':formReserva}
    return render(request, 'Elementos/Reserva/crear_reserva.html', data)


# Permite editar un Cargp por ID
def editarReserva(request, id_reserva):
    reservaObject = get_object_or_404(Reserva, id=id_reserva)
    formReserva = ReservaForm(instance=reservaObject)

    if request.method == 'POST':
        formReserva = ReservaForm(request.POST, instance=reservaObject)
        if formReserva.is_valid():
            formReserva.save()
            return HttpResponseRedirect(reverse('data_reserva'))
    
    data = {'formKey':formReserva}
    return render(request, 'Elementos/Reserva/crear_reserva.html', data)


# Permite eliminar un Reserva por ID
def eliminarReserva(request, id_reserva):
    reservaObject = get_object_or_404(Reserva, id=id_reserva)
    reservaObject.delete()

    return HttpResponseRedirect(reverse('data_reserva'))


# !================= VISTAS CRUD DE LA API CON Django Framework ==========================

# .===================|CRUD PARA EL EMPLEADO|=======================
# Funcion para MOSTRAR todos los reservas y CREAR un solo reserva
@api_view(['GET','POST'])
def reservaDataApi(request):

    # MUESTRA TODOS LOS EMPLEADOS 
    if request.method == 'GET':
        reservaObject = Reserva.objects.all()
        serializerData = ReservaSerializer(reservaObject, many=True)
        return Response(serializerData.data)

    # CREA UN SOLO EMPLEADO
    if request.method == 'POST':
        serializerData = ReservaSerializer(data=request.data)
        if serializerData.is_valid():
            serializerData.save()
            return Response(serializerData.data, status=status.HTTP_201_CREATED)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)


# Funcion para MOSTRAR, EDITAR Y ELMINAR SOLO un reserva por PK
@api_view(['GET','PUT','DELETE'])
def reservaCrudApi(request, pk):

    # Validacion simple de verificacion del objeto
    try:
        reservaObject = Reserva.objects.get(pk=pk)

    except Reserva.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Obtenemos todos los datos del objeto que concuerda con la PK
    if request.method == 'GET':
        serializerData = ReservaSerializer(reservaObject)
        return Response(serializerData.data)
    
    # Editamos un reserva buscado y validamos su guardado
    if request.method == 'PUT':
        serializerData = ReservaSerializer(reservaObject, data=request.data)
        if serializerData.is_valid():
            serializerData.save()
            return Response(serializerData.data)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Permite eliminar el reserva buscado por PK
    if request.method == 'DELETE':
        reservaObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# .===================|CRUD PARA EL ESTADO|=======================
# Funcion para MOSTRAR todos los estados y CREAR un solo estado
@api_view(['GET','POST'])
def estadoDataApi(request):

    # MUESTRA TODOS LOS ESTADOS 
    if request.method == 'GET':
        estadoObject = Estado.objects.all()
        serializerData = EstadoSerializer(estadoObject, many=True)
        return Response(serializerData.data)

    # CREA UN SOLO ESTADO
    if request.method == 'POST':
        serializerData = EstadoSerializer(data=request.data)
        if serializerData.is_valid():
            serializerData.save()
            return Response(serializerData.data, status=status.HTTP_201_CREATED)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)


# Funcion para MOSTRAR, EDITAR Y ELMINAR SOLO un estado por PK
@api_view(['GET','PUT','DELETE'])
def estadoCrudApi(request, pk):

    # Validacion simple de verificacion del objeto
    try:
        estadoObject = Estado.objects.get(pk=pk)

    except Estado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Obtenemos todos los datos del objeto que concuerda con la PK
    if request.method == 'GET':
        serializerData = EstadoSerializer(estadoObject)
        return Response(serializerData.data)
    
    # Editamos un estado buscado y validamos su guardado
    if request.method == 'PUT':
        serializerData = EstadoSerializer(estadoObject, data=request.data)
        if serializerData.is_valid():
            serializerData.save()
            return Response(serializerData.data)
        return Response(serializerData.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Permite eliminar el estado buscado por PK
    if request.method == 'DELETE':
        estadoObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
