from django.db import models

class Menu(models.Model):
    pass

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Item(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    precio = models.DecimalField(null=False)
    cantidad_stock = models.IntegerField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE) 

class Pedido(models.Model):
    items = models.ManyToManyField(Item)
    monto_total = models.DecimalField(null=False)

    def calcular_monto(self):
        pass

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    dni = models.IntegerField(max_length=8, unique=True, null=False)
    fecha_nacimiento = models.DateField(verbose_name="fecha nacimiento")
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

class Reserva(models.Model):
    pass

class Descuento(models.Model):
    pass
# Create your models here.
