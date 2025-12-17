from rest_framework import serializers

from reservaApp.models import Estado, Reserva


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

    def validate_estado(self, value):

        estadoObjects = Estado.objects.all()

        for estadoN in estadoObjects:

            if estadoN.estado == value:
                raise serializers.ValidationError('ERROR.. El nombre del estado debe ser diferente a los existenes')
            
        return value



class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    # VALIDACION DE LETRAS POR CANTIDAD
    def validate_nombre_persona(self, value):

        cant_letras = len(value)

        if cant_letras < 1:
            raise serializers.ValidationError("ERROR.. El nombre no puede estar vacio")
        if cant_letras > 15:
            raise serializers.ValidationError("ERROR.. El nombre no puede tener mas de 15 caracteres")

        return value
    
    # Validacion de cantida minima
    def validate_cant_persona(self, value):

        if value <= 0:
            raise serializers.ValidationError("ERROR.. La cantidad de personas debe ser superior a cero")

        return value
    








