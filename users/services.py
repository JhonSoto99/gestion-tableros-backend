from users import models

def consultar_usuario(email_user, password):
    """
    Función para consultar si un usuario existe un usuario al logearse
    :param email_user:
    :param password:
    :return: Queryset
    """
    try:
        user = models.User.objects.filter(email_user=email_user).filter(password=password).all()
        return user
    except Exception as e:
        print('Error al consultar usuario')