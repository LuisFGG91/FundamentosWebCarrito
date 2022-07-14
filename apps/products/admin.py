from django.contrib import admin

# Register your models here.importamos el modelo
from .models import Product

#generamos una nueva clase, modificaremos el comportamiento del producto en el administrador
class ProductAdmin(admin.ModelAdmin):
    #que campos deseamos ver en el formulario?
    fields = ('title', 'description', 'price', 'image')
    list_display = ('__str__','slug','created_at')

#registramos el modelo
admin.site.register(Product, ProductAdmin)
