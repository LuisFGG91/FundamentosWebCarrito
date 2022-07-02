from django.contrib import admin
from apps.usuarios.models import AlumnoProfile, Comuna, ProfesorProfile, Region, UTPProfile, Usuario

admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(AlumnoProfile)
admin.site.register(ProfesorProfile)
admin.site.register(UTPProfile)

