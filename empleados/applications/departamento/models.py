from django.db import models

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=50)
    is_active = models.BooleanField('Activo', default=True)
    
    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Departamentos de la empresa'
        ordering = ['name']
        unique_together = ('name', 'shor_name')

    def __str__(self):
        return str(self.id) + '-' + self.name
