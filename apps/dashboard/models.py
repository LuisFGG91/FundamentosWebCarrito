from pyexpat import model
from django.db import models
from apps.usuarios.models import User
from django.utils import timezone
from django.db import connections, migrations, models


class Dashboard(models.Model):
    
    name = models.CharField(('name'), max_length=150, blank=True)
    
    class Meta:
        db_table = 'dash'