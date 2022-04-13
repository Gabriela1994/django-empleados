from django.contrib import admin
from applications.persona.models import Empleado, Habilidades

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "departamento",
        'job',
        'full_name',
    )
    #agregar un atributo que no existe en la tabla de sql
    def full_name(self, obj):
        print(obj.first_name)
        return obj.first_name + ' '+ obj.last_name
    
    search_fields = ('first_name',)
    list_filter = ('job', 'habilidades',)
    #solo para muchos a muchos
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)