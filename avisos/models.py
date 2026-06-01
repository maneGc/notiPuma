from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    

class Aviso(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='avisos')

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo