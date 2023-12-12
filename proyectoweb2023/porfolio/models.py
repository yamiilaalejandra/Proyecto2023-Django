from django.db import models

# Create your models here.
class Project(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField(max_length=20)
    imail = models.TextField()
    create  = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)