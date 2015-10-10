from django.db import models

# Create your models here.

class franquicia(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=200)
	## Campo imagen
	activo = models.BooleanField(default = 'true')
