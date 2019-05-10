from django.contrib import admin
from users import models

class UserAdmin(admin.ModelAdmin):
    """
    Clase para administrar los Usuarios
    """
    list_display = ('email_user', 'password', 'num_documento', 'nombres', 'apellidos')

    fieldsets = (
        ('INFORMACION_BASICA', {
            'fields': ('email_user', 'password', 'num_documento', 'nombres', 'apellidos')
        }),
    )

    def save_model(self, request, obj, form, change):
        super(UserAdmin, self).save_model(request, obj, form, change)

admin.site.register(models.User, UserAdmin)