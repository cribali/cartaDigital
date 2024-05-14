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
    cantidad_seleccionada = models.IntegerField(null=True)
    cantidad_stock = models.IntegerField(null=False)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)

class Pedido(models.Model):
    items = models.ManyToManyField(Item)
    monto_total = models.DecimalField(null=False, default=0)

    def calcular_monto(self):
        pedido = Pedido.objects.get(pk=pedido.id)
        monto_total = 0
        for item in pedido.items.all():
            monto_total += item.precio * item.cantidad_seleccionada
        self.monto_total = monto_total
        pedido.save()

class Cliente(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    dni = models.IntegerField(max_length=8, unique=True, null=False)
    fecha_nacimiento = models.DateField(verbose_name="fecha nacimiento")
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad_personas = models.IntegerField(null=False)
    fecha_hora = models.DateTimeField(null=False)

class Descuento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    porcentaje = models.DecimalField(null=True)
# Create your models here.
