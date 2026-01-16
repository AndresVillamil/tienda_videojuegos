from django.shortcuts import render

# Vista de la página de inicio
def index(request):
    # render toma el reques y el archvo html que queremos mostrar
    return render(request, 'home/index.html')   

# Vista de la página de contacto
def contacto(request):
    return render(request, 'home/contacto.html')