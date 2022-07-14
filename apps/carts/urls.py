from django.urls import path

from . import views

app_name = 'carts'

#vista http://127.0.0.1:8000/carrito/agregar

urlpatterns = [
    path('',views.cart, name='cart'),
    path('agregar', views.add, name='add'),
    path('eliminar', views.remove, name='remove')
]
