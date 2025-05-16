from django.contrib import admin
from .models import Producto  # Asegúrate de tener este modelo creado

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'talla', 'precio', 'stock')
    search_fields = ('modelo', 'marca')
    list_filter = ('marca', 'talla')
