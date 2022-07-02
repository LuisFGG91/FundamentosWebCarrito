
from django.urls import path, re_path
from apps.perfiles import views as vw 


urlpatterns = [
    # The home page
#    re_path(r'', folio.index, name='home'),
    
    re_path(r'^perfiles/(?:(?P<action>\w+)/)?(?:(?P<id>\w+)/)?', vw.perfilesView.as_view(),name='perfiles'),
    # Matches any html file
#    re_path(r'^.*\.*', folio.pages, name='pages'),

]