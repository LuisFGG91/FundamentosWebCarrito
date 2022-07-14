from .models import Cart

def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None
    #nueva variable
    cart_id = request.session.get('cart_id') #obtenemos el cart_id
    cart = Cart.objects.filter(cart_id=cart_id).first() #obtenemos el carrito
    #si no existe lo creamos
    if cart is None:
        cart = Cart.objects.create(user=user)

    #si el usuario existe(se encuentra autenticado) y no posee usuario
    if user and cart.user is None:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id

    return cart
