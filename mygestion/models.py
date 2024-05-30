from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

class tarea(models.Model):
    titulo= models.CharField(max_length=200)
    descripcion=models.TextField()
    proyecto= models.ForeignKey(Project, on_delete=models.CASCADE)

class Usuario(models.Model):
    nombre= models.CharField(max_length=200)
    apellido=models.CharField(max_length=64)
    password= models.CharField(max_length=64)

