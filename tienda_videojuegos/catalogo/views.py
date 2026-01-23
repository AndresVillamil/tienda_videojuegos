from django.shortcuts import render
from django.core.paginator import Paginator
from catalogo.models import Juego

# Create your views here.
def lista_juegos(request):
    juegos = Juego.objects.all().order_by('id')#mantenemos el orden por id
    
    paginator = Paginator(juegos, 6) # Mostrar 6 juegos por página

    #obtenemos el numero de página desde la URL (? page=2)
    page_number = request.GET.get('page')

    #Obtenemos los objetos de esa página
    page_obj = paginator.get_page(page_number)

    contexto_catalogo_juegos = {
        'lista_juegos': page_obj
    }
    
    return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos)