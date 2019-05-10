# third parties
from rest_framework import routers
from django.conf.urls import url

# local
from users.views import *

router = routers.SimpleRouter()
router.register(r'user', UserCreateViewSet)


urlpatterns = [
    url(r'^login/$',ConsultarUsuario.as_view(), name='user.get'),

    ] + router.urls
