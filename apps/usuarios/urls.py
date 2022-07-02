
from django.urls import path, re_path
from apps.usuarios import views as vw 


urlpatterns = [
    # The home page
#    re_path(r'', folio.index, name='home'),
    
    re_path(r'^usuarios/(?:(?P<action>\w+)/)?(?:(?P<id>\w+)/)?', vw.usuariosView.as_view(),name='usuarios'),
    # Matches any html file
#    re_path(r'^.*\.*', folio.pages, name='pages'),

]