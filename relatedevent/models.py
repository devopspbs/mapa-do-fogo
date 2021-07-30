from django.conf import settings # new
from django.contrib import auth
from django.contrib.gis.db import models
#from django.db import models
from hashid_field import HashidField, HashidAutoField

# Create your models here.

class ReportedEvent(models.Model):
    #Fields
    id = HashidAutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    coordenada = models.PointField()
    user_agent = models.TextField(blank=True)
    reported_hash = HashidField(blank=True, null=True)
    
    class Meta: 
        ordering = ('created',) 