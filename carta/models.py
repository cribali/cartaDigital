from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)

    def __str__(self):
        return self.nombre

class clasificacion(models.Model):
    nombre= models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Bebida(models.Model):
    nombre= models.CharField(max_length=50)
    tipo= models.ForeignKey(clasificacion, on_delete= models.CASCADE)   
    precio= models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre




# Create your models here.
