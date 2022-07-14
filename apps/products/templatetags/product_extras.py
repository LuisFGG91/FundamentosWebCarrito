#importamos
from django import template

#generamos una nueva instancia
register = template.Library()

#decoramos con la funcion @
#funcion
#lo mandamos a llamar en el template add de carts
@register.filter()
def price_format(value):
    return '${0:.2}'.format(value) #retorna formato de precio
