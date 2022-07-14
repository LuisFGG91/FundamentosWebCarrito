from django.db import models

#importamos
from products.models import Product

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    #creamos la relacion entre el modelo category y  productos
    products = models.ManyToManyField(Product, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #retornamos el titulo
    def __str__(self):
        return self.title
