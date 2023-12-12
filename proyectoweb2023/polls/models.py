from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField(max_length=20)
    imail = models.EmailField()

    def __str__(self):
        return self.nombre
