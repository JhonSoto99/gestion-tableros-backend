# third parties
from rest_framework import serializers

# local
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    serializador para permitir guardar u obtener la informacion de los usuarios
    """
    class Meta:
        model = User
        fields = ('id','email_user', 'password', 'num_documento','nombres', 'apellidos',)

