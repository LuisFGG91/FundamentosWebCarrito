import uuid #cadena de caracteres pseudoaleatorio

from django.db import models
#importamos el metodo slugify
from django.utils.text import slugify
#para el metodo pre_save
from django.db.models.signals import pre_save


# Create your models here.#representacion de una tabla, atributos = columnas
class Product(models.Model):
    #columnas de la tabla PRODUCTOS
    title = models.CharField(max_length=50) #maximo de caracteres debe coincidir con el archivo forms.py
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)#valor por default
    slug = models.SlugField(null=False, blank=False, unique=True) #no valores nulos, no strings vacios, unicamente almacenar valores unicos
    image = models.ImageField(upload_to='products/', null=False, blank=False)#las imagenes se almacenar en la carpeta products
    created_at = models.DateTimeField(auto_now_add=True)  #cuando se dio de alta el producto

    #sobreescribimos el metodo save para slugs automaticos
    #def save(self, *args, **kwargs):
        #GENERAMOS EL SLUG por medio del titulo del producto
        #self.slug = slugify(self.title)
        #super(Product, self).save(*args, **kwargs)

#retornamos el nombre de "Playera para caballero"
    def __str__(self):
        return self.title

#definimos funcion para el metedo pre_save, sustituyendo al de arriba, genera un slug nuevo, aunque el titulo sea igual
def set_slug(sender, instance, *args, **kwargs):
    #validamos si el titulo es igual?
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8]) #cadena de caracteres pseudoaleatorio, numero de caracteres
            )

        instance.slug = slug

pre_save.connect(set_slug, sender=Product)
