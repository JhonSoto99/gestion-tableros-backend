
# third parties
from rest_framework import routers
from django.conf.urls import url

# local
from tableros.views import *

router = routers.SimpleRouter()
router.register(r'tablero', TableroCreateViewSet)
router.register(r'idea', IdeaCreateViewSet)

urlpatterns = [
    url(r'^get_tableros/$',ObtenerTablerosIdeas.as_view(), name='tableros.get'),
    url(r'^aprobar_idea/$', aprobar_idea, name='ideas.aprobar'),

    ] + router.urls
