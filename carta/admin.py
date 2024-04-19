from django.contrib import admin
from .models import Plato, Categoria, Bebida, clasificacion


admin.site.register(Plato)
admin.site.register(Categoria)
admin.site.register(Bebida)
admin.site.register(clasificacion)
# Register your models here.
