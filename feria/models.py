from django.db import models

class franquicia(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=200)
	imagen =models.ImageField(upload_to='imagenes', null = True)
	activo = models.BooleanField(default = 'true')

	def __str__(self):
		return self.nombre

class producto(models.Model):
	franquicia = models.ForeignKey(franquicia,limit_choices_to={'activo': True})
        nombre = models.CharField(max_length=50)
        descripcion = models.TextField(max_length=200)
	precio = models.FloatField(default = 0)
        imagen =models.ImageField(upload_to='imagenes', null = True)
        activo = models.BooleanField(default = 'true')

	def __str__(self):
		return self.nombre
