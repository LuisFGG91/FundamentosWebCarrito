import uuid

from enum import Enum

from django.db import models

from users.models import User
from carts.models import Cart

from django.db.models. signals import pre_save

class OrderStatus(Enum):
    CREATED = 'CREATED'
    PAYED = 'PAYED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'


choices = [( tag, tag.value) for tag in OrderStatus ]


# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    #un usaurio puede tener muchas ordernes de compra
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Un carrito puede tener muchas ordenes
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=choices, default=OrderStatus.CREATED)
    #cargo de envio
    shipping_total = models.DecimalField(default=5, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

def set_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = str(uuid.uuid4())  #ns permite generar un identificador unico alfanumerico

pre_save.connect(set_order_id, sender=Order)
