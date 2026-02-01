from django.contrib import admin
from .models import Carrito, ItemCarrito



# Register your models here.

#Mostrar items del carrito en el admin
class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 0   #No mostrar filas extra vacías
    readonly_fields = ('subtotal',) #Campo de solo lectura para el subtotal

#Admin para el modelo Carrito
@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'total_items', 'total_precio', 'creado', 'actualizado')
    search_fields = ('usuario__username',)
    #carritos por nombre de usuario
    inlines = [ItemCarritoInline]

@admin.register(ItemCarrito)
class ItemCarritoAdmin(admin.ModelAdmin):
    list_display = ('carrito', 'juego', 'cantidad',  'subtotal')
    list_filter = ('carrito',)
    search_fields = ( 'juego__nombre',)
    readonly_fields = ('subtotal',)
