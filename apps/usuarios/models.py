# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,Group
from django.utils.translation import gettext_lazy as _
from core.settings import MEDIA_URL_USUARIO
from django.utils import timezone
from django.contrib.auth.models import User

class Region(models.Model):
    name = models.CharField(max_length=120,verbose_name="name")
    romanNumber = models.CharField(max_length=120,verbose_name="roman Number")
    number = models.IntegerField(verbose_name = 'numero')
    codigo = models.CharField(max_length=5,verbose_name="name")
    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'    
        db_table = 'users_region'  
        
class Comuna(models.Model):
    region = models.ForeignKey(Region,null=False,blank=False,on_delete=models.CASCADE)
    name = models.CharField(max_length=120,verbose_name="name")
    codigo = models.CharField(max_length=120,verbose_name="roman Number")
    class Meta:
        db_table = 'users_comuna'    
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'            
def upload_to(instance, filename):
    return MEDIA_URL_USUARIO + '/teams/{username}/profile/{filename}'.format(username=instance.user.id, filename=filename)
def upload_to_banner(instance, filename):
    return MEDIA_URL_USUARIO + '/teams/{username}/banner/{filename}'.format(username=instance.user.id, filename=filename)
class Usuario(models.Model):
    user = models.OneToOneField(User,null=True,blank=False,on_delete=models.CASCADE)
    GENERO = (('M','Masculino'),('F','Femenino'),('O','Otro'))
    image = models.ImageField(upload_to= upload_to , default='logo.png',blank=True)
    imageBanner = models.ImageField(upload_to=upload_to_banner, default='logo.png',blank=True)
    rut = models.CharField(max_length=13,help_text="Indique su RUT",verbose_name="Rut")
    phone=models.CharField(max_length=100,help_text="Numero de Teléfono. ej: +56555555555",verbose_name="Teléfono" ,null = True)
    fecha_nacimiento = models.DateField( help_text="Fecha de Nacimiento",verbose_name="Fec. Nac.",null = True)
    sexo = models.CharField(max_length=1,help_text="Masculino o Femenino",verbose_name="Sexo",choices=GENERO)
    tipo_sangre=models.CharField(max_length=5,help_text="Tipo de Sangre. ej: ORH-",verbose_name="Tipo de Sangre")
    comuna = models.ForeignKey(Region,null=True,blank=False,on_delete=models.CASCADE)
    direccion= models.CharField(max_length=55,help_text="Dirección de Habitación",verbose_name="Domicilio",default="",null = True)
    numero=models.CharField(max_length=8,help_text="Numero",verbose_name="Numero",default="",null = True)    
    is_profesor = models.BooleanField('Es profesor',default=False)
    is_alumno = models.BooleanField('Es alumno',default=False)
    is_utp = models.BooleanField('Es utp',default=False)
    
    class Meta:
        db_table = 'users_usuario'  
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios' 
    def get_image(self):
        if self.image:
            return'{}'.format(self.image)
        return'{}{}'.format(MEDIA_URL_USUARIO,'teams/logo1.png')
    def get_imageBanner(self):
        if self.imageBanner:
            return'{}'.format(self.imageBanner)
        return'{}{}'.format(MEDIA_URL_USUARIO,'teams/logo.png')

class Customer(User):
    class Meta:
        proxy = True
#retornar todos los productos adquiridos por el cliente
    def get_products(self):
        #retornamos una lista vacia
        return []

#si tenemos la necesidad de agregar nuevos campos y atrubutos osbre el modelo user, generamos una relacion uno a uno
#creamos un nuevo modelo
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)#CUANDO UN USUARIO SEA ELIMINADO TAMBIEN SE ELIMINE EL REGISTRO PROFILE
    bio = models.TextField()

