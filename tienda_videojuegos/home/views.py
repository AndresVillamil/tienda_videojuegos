from django.shortcuts import render
from catalogo.models import Juego

# Vista de la página de inicio
def index(request):
    # render toma el reques y el archvo html que queremos mostrar
    return render(request, 'home/index.html')   

# Vista de la página de contacto
def contacto(request):
    return render(request, 'home/contacto.html')

def home(request):
    juegos_destacados = Juego.objects.filter(activo=True)[:8]

    return render(request, 'index.html', {
        'juegos_destacados': juegos_destacados
    })

