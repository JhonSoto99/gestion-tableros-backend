from django.db import models
from users.models import User as user_model

CHOICES_TIPO_TABLERO = (
    ('PRIVADO', 'PRIVADO'),
    ('PUBLICO', 'PÚBLICO'),
)

CHOICES_SI_NO = (
    ('SI', 'SI'),
    ('NO', 'NO'),
)

# Modelo Abstracto para registrar las fechas de los registros y llevar una trazabilidad
class TimeStampedModel(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True,
                                          verbose_name="fecha de creación")
    fecha_modificacion = models.DateTimeField(
        auto_now_add=False, auto_now=False, null=True, blank=True,
        verbose_name="fecha de modificación")

    class Meta:
        abstract = True

# Modelo para registrar los tableros
class Tablero(TimeStampedModel):
    titulo = models.CharField(max_length=100, null=False, blank=False, verbose_name="Titulo")
    descripcion = models.TextField(max_length=500, null=False, blank=False, verbose_name="Descripción")
    tipo_tablero = models.CharField(choices=CHOICES_TIPO_TABLERO, max_length=30, null=False, blank=False, verbose_name="Tipo de tablero", help_text='Si es público o privado')
    creado_por = models.ForeignKey(user_model, null=False, blank=False, related_name='tablero_creado_por',
                                   verbose_name="Creado Por", on_delete=models.PROTECT)
    modificado_por = models.ForeignKey(user_model, null=True, blank=True,related_name='tablero_modificado_por',
                                       verbose_name="Modificado Por", on_delete=models.PROTECT)

    def creado_por_username(self):
        if self.creado_por != None:
           return "%s" % user_model.objects.get(id=self.creado_por.id)
        else:
           return ""

    class Meta:
        verbose_name = 'Tablero'
        verbose_name_plural = 'Tableros'
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.titulo


    def save(self, *args, **kwargs):
        return super(Tablero, self).save(*args, **kwargs)

# Modelo para registrar las ideas
class Idea(TimeStampedModel):
    tablero = models.ForeignKey(Tablero, null=False, blank=False, verbose_name="Tablero", on_delete=models.CASCADE,
                               help_text="Tablero al que pertenece la idea")
    descripcion = models.TextField(max_length=500, null=False, blank=False, verbose_name="Descripción")
    creado_por = models.ForeignKey(user_model, null=True, blank=False, related_name='idea_creado_por',
                                   verbose_name="Creado Por", on_delete=models.SET_NULL)
    modificado_por = models.ForeignKey(user_model, null=True, blank=True, related_name='idea_modificado_por',
                                       verbose_name="Modificado Por", on_delete=models.SET_NULL)
    aprobada = models.CharField(choices=CHOICES_SI_NO, null=False, blank=False, verbose_name="aprobada", max_length=2)


    class Meta:
        verbose_name = 'Idea'
        verbose_name_plural = 'Ideas'
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        return super(Idea, self).save(*args, **kwargs)