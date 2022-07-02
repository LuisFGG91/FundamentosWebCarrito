
from django.db import models

# Create your models here.

class Periodo(models.Model):
    
    anno = models.IntegerField(verbose_name = 'Año')
    fecha_inicio = models.DateField( help_text="Fecha de inicio",verbose_name="Fec. ini.")
    fecha_fin = models.DateField( help_text="Fecha de fin",verbose_name="Fec. fin.")
    
    class Meta:
        db_table = 'peri'   
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos' 
        