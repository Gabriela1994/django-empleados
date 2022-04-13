from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidades = models.CharField('Habilidades', max_length=50)

    class Meta():
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
    
    def __str__(self):
        return str(self.id) + '-' + self.habilidades

class Empleado(models.Model):
    JOB_CHOICES= (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otros'),
    )

    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #imagen = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name