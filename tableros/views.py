from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import views

from tableros.models import Tablero, Idea
from tableros.serializers import TableroCreateSerializer, IdeaCreateSerializer


class TableroCreateViewSet(ModelViewSet):
    """
    create:
    Creacion de un Tablero

    retrieve:
    Obtención de un Tablero por id

    update:
    Modificación de un Tablero por id

    destroy:
    Eliminación de un Tablero por id
    """
    permission_classes = (AllowAny,)
    queryset = Tablero.objects.all()
    serializer_class = TableroCreateSerializer


class IdeaCreateViewSet(ModelViewSet):
    """
    create:
    Creacion de una Idea

    retrieve:
    Obtención de una Idea por id

    update:
    Modificación de una Idea por id

    destroy:
    Eliminación de una Idea por id
    """
    permission_classes = (AllowAny,)
    queryset = Idea.objects.all()
    serializer_class = IdeaCreateSerializer


class ObtenerTablerosIdeas(views.APIView):
    """
    Obtencion de todos los tableros con sus respectivas ideas
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        titulo = request.GET.get('titulo')
        tableros = self.get_tableros(titulo)
        ideas = self.get_ideas()



        response = [tableros, ideas]
        return Response(response)

    def get_tableros(self, titulo):
        if titulo and titulo != 'undefined':
            tableros = Tablero.objects.filter(titulo__contains=titulo).all()
        else:
            tableros = Tablero.objects.all()
        if tableros == None:
            return Response(status=404)
        tableros_serializer = TableroCreateSerializer(tableros, many=True)
        return tableros_serializer.data

    def get_ideas(self):
        ideas = Idea.objects.all()
        ideas_serializer = IdeaCreateSerializer(ideas, many=True)
        return ideas_serializer.data


def aprobar_idea(request):
    """
    Funcion para aprobar las ideas de otros usuarios
    :param request:
    :return:Json
    """
    import json
    from django.http import HttpResponse
    default_content_type = 'application/json; charset=UTF-8'
    try:
        id = request.GET.get('id')
        if not id:
            raise Exception("id requerido...")
        idea = Idea.objects.get(id=id)
        idea.aprobada = 'SI'
        idea.save()
        return HttpResponse(json.dumps({
                             'success': True,
                             'result': idea
                         }), content_type=default_content_type)
    except Exception as e:
        return HttpResponse(json.dumps({
            'success': False,
            'errors': e.args
        }), content_type=default_content_type)






