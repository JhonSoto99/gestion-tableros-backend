from django.db import models

# Modelo para guardar información de los usuarios
class User(models.Model):
    email_user = models.CharField(max_length=120, null=True, blank=True, verbose_name='usuario o email')
    password = models.CharField(max_length=120, null=True, blank=True, verbose_name='contraseña')
    num_documento = models.CharField(max_length=120, null=True, blank=True, verbose_name='número de documento')
    nombres = models.CharField(max_length=120, null=True, blank=True, verbose_name='nombres')
    apellidos = models.CharField(max_length=120, null=True, blank=True, verbose_name='apellidos')


    def __str__(self):
        return self.email_user

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'usuarios'

    def save(self, *args, **kwargs):
        return super(User, self).save(*args, **kwargs)
