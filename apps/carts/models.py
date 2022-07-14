import uuid
import decimal

from django.db import models

from users.models import User
from products.models import Product

from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.db.models.signals import m2m_changed


# Create your models here.
class Cart(models.Model):
    #identificador unico
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey (User, null=True, blank=True, on_delete=models.CASCADE) #si un usuario es eliminado se elimina su relacion
    products = models.ManyToManyField(Product, through='CartProducts')#muchos a muchos, un producto puede encontrase en muchos carritos
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total =  models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    #comision del producto
    FEE = 0.05 #5% DE COMISION

    #retorna el id del carrito
    def __str__(self):
        return self.cart_id

    #sub-total carrito
    def update_totals(self):
        self.update_subtotal()
        self.update_total()
#sub-total carrito
    def update_subtotal(self):
        #suma de pecio de productos
        self.subtotal = sum([
            cp.quantity * cp.product.price for cp in self.products_related()
         ])
        self.save()
#sub-total carrito
    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal( Cart.FEE ))
        self.save()

    def products_related(self):
        return self.cartproducts_set.select_related('product')
#PARA NO OBTENER DOS VISTAS AL MOMENTO DE GENERAR MAS CANTIDADES
class CartProductsManager(models.Manager):

    def create_or_update_quantity(self, cart, product, quantity=1):
        object, created = self.get_or_create(cart=cart, product=product)

        if not created:
            object.quantity +=quantity
            object.save()
        return object

#definimos modelo para la cantidad de productos
class CartProducts(models.Model):
    #un carrito puede tener muchos cart products y cart products puede tener varios carritos
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #cuanto de un producto agregamos a un carrito
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CartProductsManager()

def set_cart_id(sender, instance, *args, **kwargs):
    #si no posee id
    if not instance.cart_id:
        instance.cart_id= str(uuid.uuid4())

#calcular total
def update_totals(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear': #despues de que se agrega al carrito,despues de eliminar un producto, despues de que carrito se limpia
        instance.update_totals()

def post_save_update_totals(sender, instance, *args, **kwargs):
    instance.cart.update_totals()

pre_save.connect(set_cart_id, sender=Cart)
#de views.py
post_save.connect(post_save_update_totals, sender=CartProducts)
#registramos callback, para calcular el subtotal y total
m2m_changed.connect(update_totals, sender=Cart.products.through)

    #un usuario puede tener muchos carrito_compras,relacion uno a muchos
            #carrito de copmpras pueda o no pertencerla a un usuario
