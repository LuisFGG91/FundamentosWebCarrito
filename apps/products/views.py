from django.shortcuts import render
#EJECUTAMOS UNA CONSULTA aplicando diferentes filtros
from django.db.models import Q

#importamos la clase ListView
from django.views.generic.list import ListView
#importamos la clase DetailView
from django.views.generic.detail import DetailView

#importamos modelo products
from .models import Product

# Create your views here.
class ProductListView(ListView):
    #nombre del template que vamos a utilizar
    template_name='index.html'
    #consulta para obvtener el listado de objetos
    queryset = Product.objects.all().order_by('-id')


    #pasa el contexto de la clase al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Productos en oferta'
        context['products'] = context['product_list']

        print(context)

        return context

#obtiene un objeto un registro, la busqyeda se hara por id
class ProductDetailView(DetailView):
    #con que modelo vamos a trabajar? con el de Product
    model = Product
    #co que template vamos a trabajar?
    template_name='products/product.html'

    #pasa el contexto de la clase al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'candiblue.com'
        print(context)

        return context

class ProductSearchListView(ListView):
    template_name= 'products/search.html'

    #EJECUTAMOS UNA CONSULTA aplicando diferentes filtros
    #buscamos por el nombre del producto Y buscamos en la tabala category
    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
        return Product.objects.filter(filters)

    #SELECT * FROM products where title like %value%
    def get_queryset(self):
        #visualizaremos los productos con la categoria
        return Product.objects.filter(title__icontains=self.query())

    def query(self):
        return self.request.GET.get('q')

    #pasa el contexto de la clase al template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        #numero de productos en la lista?
        context['count'] = context['product_list'].count()

        return context
