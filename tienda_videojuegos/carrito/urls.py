from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:juego_id>/', views.agregar_al_carrito, name='agregar'),
    path('quitar/<int:juego_id>/', views.quitar_uno, name='quitar'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_item'),
    path('limpiar/', views.limpiar_carrito, name='limpiar'),
]
