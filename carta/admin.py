from django.contrib import admin
from .models import Item, Categoria, Cliente, Menu, Pedido,Reserva, Descuento


admin.site.register(Item)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Menu)
admin.site.register(Pedido)
admin.site.register(Reserva)
admin.site.register(Descuento)
# Register your models here.
