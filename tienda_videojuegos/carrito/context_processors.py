from .models import Carrito
from django.db.models import Sum

def carrito_total(request):
    carrito_count = 0

    if request.user.is_authenticated:
        carrito = Carrito.objects.filter(usuario=request.user).first()

        if carrito:
            carrito_count = (
                carrito.items.aggregate(total=Sum('cantidad'))['total']
                or 0
            )

    return {
        'carrito_count': carrito_count
    }
