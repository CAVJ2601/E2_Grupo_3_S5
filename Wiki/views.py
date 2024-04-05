from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Wiki/menuprincipal_wiki.html')

def micuenta(request):
    return render(request, 'Wiki/micuentatf.html')

def animales(request):
    return render(request, 'Wiki/Animales.html')

def armas(request):
    return render(request, 'Wiki/Armas.html')

def construcciones(request):
    return render(request, 'Wiki/Construcciones.html')

def consumibles(request):
    return render(request, 'Wiki/Consumibles.html')

def enemigos(request):
    return render(request, 'Wiki/Enemigos.html')

def flora(request):
    return render(request, 'Wiki/Flora.html')

def foro(request):
    return render(request, 'Wiki/forowiki.html')

def ini_sesion(request):
    return render(request, 'Wiki/inicio_sesion_wiki.html')

def logros(request):
    return render(request, 'Wiki/Logros.html')

def lugares(request):
    return render(request, 'Wiki/Lugarestf.html')

def recuperarcontra(request):
    return render(request, 'Wiki/recuperarcontra.html')

def registro(request):
    return render(request, 'Wiki/registrase_wiki.html')