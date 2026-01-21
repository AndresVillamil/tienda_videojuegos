from django.shortcuts import render

# Create your views here.
def lista_juegos(request):
    juegos = [
        {'nombre': 'The Legend of Zelda: Breath of the Wild', 'precio': 59.99, 'plataforma': 'Nintendo Switch'},
        {'nombre': 'God of War', 'precio': 39.99, 'plataforma': 'PlayStation 4'},
        {'nombre': 'Halo Infinite', 'precio': 49.99, 'plataforma': 'Xbox Series X'},
        {'nombre': 'Cyberpunk 2077', 'precio': 29.99, 'plataforma': 'PC'},
        {'nombre': 'Minecraft', 'precio': 26.95, 'plataforma': 'Multiplataforma'},
        {'nombre': 'Among Us', 'precio': 4.99, 'plataforma': 'Multiplataforma'},
        {'nombre': 'Red Dead Redemption 2', 'precio': 59.99, 'plataforma': 'PlayStation 4'},
        {'nombre': 'The Witcher 3: Wild Hunt', 'precio': 39.99, 'plataforma': 'PC'}
    ]
    contexto_catalogo_juegos = {
        'lista_juegos': juegos
    }
    
    return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos)