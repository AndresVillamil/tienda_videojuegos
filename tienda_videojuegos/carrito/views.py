from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalogo.models import Juego
from .models import Carrito, ItemCarrito

# Create your views here.
@login_required
def agregar_al_carrito(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, juego=juego)

    if not creado:
        item.cantidad += 1
        item.save()

    return redirect('catalogo:detalle_juego', pk=juego.id)

@login_required
def ver_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.items.select_related('juego')
    total = carrito.total_precio()

    contexto = {
        'carrito': carrito,
        'items': items,
        'total': total,
    }

    return render(request, 'carrito/ver_carrito.html', contexto)

@login_required
def eliminar_del_carrito(request, item_id):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    item = get_object_or_404(ItemCarrito, id=item_id, carrito=carrito)
    item.delete()
    return redirect('carrito:ver_carrito')

@login_required
def quitar_uno(request, juego_id):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

    item = carrito.items.filter(juego_id=juego_id).first()

    if item:
        if item.cantidad > 1:
            item.cantidad -= 1
            item.save()
        else:
            item.delete()

    return redirect('carrito:ver_carrito')




@login_required
def limpiar_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    carrito.items.all().delete()
    return redirect('carrito:ver_carrito')