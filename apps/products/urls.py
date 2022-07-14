from django.urls import path

from . import views

#todas las rutas le pertecenen a la aplicacion products
app_name = 'products'

urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product'), #primary key

]
