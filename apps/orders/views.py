from django.shortcuts import render

from .utils import get_or_create_order
from carts.utils import get_or_create_cart

#importamos modelo
from .models import Order

# Create your views here.
def order(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)
    
    return render(request, 'orders/order.html',{

    })
