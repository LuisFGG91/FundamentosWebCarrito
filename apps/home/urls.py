

from django.urls import path, re_path , include
from apps.home import views
from core.settings import MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    re_path('^', include("apps.dashboard.urls")),     

    re_path('^', include("apps.actividades.urls")),
    re_path('^', include("apps.asistencias.urls")),  
    re_path('^', include("apps.bibliotecas.urls")),   
    re_path('^', include("apps.cursos.urls")),            
    re_path('^', include("apps.evaluaciones.urls")),         
    re_path('^', include("apps.inscripciones.urls")),         
    re_path('^', include("apps.materias.urls")),       
    re_path('^', include("apps.alumnos.urls")),       
    re_path('^', include("apps.perfiles.urls")),         
    re_path('^', include("apps.profesores.urls")),
    re_path('^', include("apps.usuarios.urls")),   
    re_path(r'^.*\.*', views.pages, name='pages'),

]+ static(MEDIA_URL)
