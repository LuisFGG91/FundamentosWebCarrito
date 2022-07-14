

from django.shortcuts import render

from django.shortcuts import redirect
#importamos 404
from django.shortcuts import get_object_or_404

#importamos CartProducts
from .models import CartProducts

from products.models import Product

from .models import Cart
from .utils import get_or_create_cart

# Create your views here.
def cart(request):
    #este codigo se encuentra en el archivo utils.py
    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html',{
        'cart':cart

    })

#registramos una nueva vista en el carrito de compras, obteneos el producto del carrito de compras
def add(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    #cantidad de productos
    quantity = int(request.POST.get('quantity', 1))
    #agregamos un producto al carrito

    #cart.products.add(product, through_defaults={
        #'quantity':quantity
    #})
    #generamos instancia de from .models ....CartProducts
    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart,
                                                                    product=product,
                                                                    quantity=quantity)

    return render(request, 'carts/add.html', {
        'quantity':quantity,
        'cart_product':cart_product,
        'product':product

    })

def remove(request):

    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    #deshacemos la relacion
    cart.products.remove(product)
    #redirigimos a la vista del carritos
    return redirect('carts:cart')






#creamos una sesion
#request.session['cart_id'] = '123'

#obtener el valor de una session
#valor = request.session.get('cart_id')
#print(valor)

#eliminar una session
#request.session['cart_id'] = None
