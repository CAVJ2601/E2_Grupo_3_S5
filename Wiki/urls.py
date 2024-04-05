from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='Pagina Principal'),
    path('animales/', animales, name='Animales'),
    path('armas/', armas, name='Armas'),
    path('construcciones/', construcciones, name='Construcciones'),
    path('consumibles/', consumibles, name='Consumibles'),
    path('enemigos/', enemigos, name='Enemigos'),
    path('flora/', flora, name='Flora'),
    path('foro/', foro, name='Foro'),
    path('inisesion/', ini_sesion, name='Inicio Sesion'),
    path('logros/', logros, name='Logros'),
    path('lugares/', lugares, name='Lugares'),
    path('micuenta/', micuenta, name='Mi Cuenta'),
    path('recuperarcontra/', recuperarcontra, name='Recuperar Contraseña'),
    path('registro/', registro, name='Registrarse'),
]