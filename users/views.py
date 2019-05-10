from users.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import views
from rest_framework.permissions import AllowAny
from users import services
from .serializers import UserSerializer

import json
from django.http import HttpResponse
default_content_type = 'application/json; charset=UTF-8'


class UserCreateViewSet(ModelViewSet):
    """
    create:
    Creacion de un Usuario

    retrieve:
    Obtención de un Usuario por id

    update:
    Modificación de un Usuario por id

    destroy:
    Eliminación de un Usuario por id
    """
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ConsultarUsuario(views.APIView):
    """
    Clase para consultar si existe un usuario
    :return: Json
    """
    permission_classes = (AllowAny,)

    def get_object(self, email_user, password):
        user = services.consultar_usuario(email_user, password)
        if user:
            return user
        return False

    def get(self, request, format=None):
        email_user = request.GET.get('email_user')
        password = request.GET.get('password')
        user = self.get_object(email_user, password)
        if user:
            return HttpResponse(json.dumps({
                'success': True,
                'id': user[0].id,
                'user': user[0].email_user,
            }), content_type=default_content_type)
        else:
            return HttpResponse(json.dumps({
                'success': False,
                'errors': "usuario no existe"
            }), content_type=default_content_type)

