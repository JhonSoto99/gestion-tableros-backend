# third parties
from rest_framework import serializers

# local
from .models import Tablero, Idea


class TableroCreateSerializer(serializers.ModelSerializer):
    """
    serializador para guardar u obtener la informacion de los tableros
    """
    creado_por_username = serializers.CharField(required=False) # Item personalizado para obtener el nombre del usuario creador
    class Meta:
        model = Tablero
        fields = ('id','titulo', 'descripcion', 'tipo_tablero', 'creado_por', 'creado_por_username')

class IdeaCreateSerializer(serializers.ModelSerializer):
    """
    serializador para guardar u obtener la informacion de las ideas
    """
    class Meta:
        model = Idea
        fields = ('id','tablero', 'descripcion', 'aprobada', 'creado_por')