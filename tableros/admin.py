from django.contrib import admin
from tableros import models

class TableroAdmin(admin.ModelAdmin):
    """
    Administrador para la gestion de Tableros
    """
    list_display = ('titulo', 'descripcion', 'tipo_tablero')

    fieldsets = (
        ('INFORMACION_BASICA', {
            'fields': ('titulo', 'descripcion', 'tipo_tablero', 'creado_por')
        }),
    )

    def save_model(self, request, obj, form, change):
        super(TableroAdmin, self).save_model(request, obj, form, change)


class IdeaAdmin(admin.ModelAdmin):
    """
    Administrador para la gestion de Ideas relacionadas a un tablero
    """
    list_display = ('tablero', 'descripcion')

    fieldsets = (
        ('INFORMACION_BASICA', {
            'fields': ('tablero', 'descripcion', 'aprobada', 'creado_por')
        }),
    )

    def save_model(self, request, obj, form, change):
        super(IdeaAdmin, self).save_model(request, obj, form, change)


admin.site.register(models.Tablero, TableroAdmin)
admin.site.register(models.Idea, IdeaAdmin)