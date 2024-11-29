from django.db import models

# Create your models here.
class Estudiantes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.edad}'
