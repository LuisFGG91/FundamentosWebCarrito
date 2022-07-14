

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render,get_object_or_404



def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))
    #return redirect('dashboardView')	
#Importamos nueva funcion para renderizar - renderizar template - video
from django.shortcuts import render
#importamos funcion para redireccion
from django.shortcuts import redirect

#importamos funcion para decirle al usuario si entro o no
from django.contrib import messages

#Hola Mundo - Video
#from django.http import HttpResponse

#generamos el login
from django.contrib.auth import login
#Nos delogeamos
from django.contrib.auth import logout
#autenticación para usuarios, concocer si existe en la BD
from django.contrib.auth import authenticate
#funcion que permite que crear/dar de alta usuarios
#from django.contrib.auth.models import User
from apps.usuarios.models import User

#registrar RegisterForm()
from .forms import RegisterForm

#importamos el modelo productos
from products.models import Product


"""renderiza el template index.html
def index(request):
    return render(request,'index.html', {
        'message': 'Candelaria.com.mx',
        'title': 'Carrito de compras',
        'productos': [
            {'Titulo': 'Playera', 'Precio':5, 'Stock': True},
                {'Titulo': 'Camisa', 'Precio':5, 'Stock': True},
            {'Titulo': 'Mochila', 'Precio':5, 'Stock': False}
        ]
    })"""

def index(request):
    #ordena los productos por el mas reciente
    products = Product.objects.all().order_by('-id')

    #para cambiar el title de la pestaña tenemos que hacerlo en views.py de products
    return render(request,'index.html', {
        'message': 'candiblue.com',
        'title': 'Carrito de compras',
        'products': products,
    })

def login_view(request):
    #si el usuario esta autenticado y quiere
    #ingresar por medio de la url "http://127.0.0.1:8000/usuarios/login"
    #lo redireccionara al index
    if request.user.is_authenticated:
        return redirect('index')



    if request.method == 'POST': #como se esta obteniendo la informacion, metodo get o post
         username = request.POST.get('username')
         password = request.POST.get('password')

         #autenticación y login
         user = authenticate(username=username, password=password)
         if user:
             login(request, user)
             #mensaje de exito, ya que login se realizo correctamente
             messages.success(request, 'Bienvenido!, {}'.format(user.username))
             return redirect('index')
         else:
            messages.error(request, 'Usuario o Contraseña NO VALIDOS :( ')

    return render(request, 'users/login.html', {

    })

def logout_view(request):
    #eliminamos sesion
    logout(request)
    messages.success(request, 'Sesion Cerrada exitosamente')
    return redirect('login')

def register(request):
    #si el usuario esta autenticado y quiere
    #ingresar por medio de la url "http://127.0.0.1:8000/usuarios/registro"
    #lo redireccionara al index
    if request.user.is_authenticated:
        return redirect('index')

    form = RegisterForm(request.POST or None)

    #leer datos del formulario
    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario Creado Exitosamente')
            return redirect('index')
            #user.save()

    return render(request, 'users/register.html', {
        'form': form #mandamos a llamar la forma, agregandola al contexto
    })

def pedidos(request):
    return render(request, 'pedidos/pedidos.html', {

    })
    #Hola Mundo - Video return HttpResponse('Hola Mundo desde el archivo views.py!')

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
