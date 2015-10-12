from django.contrib import admin

# Register your models here.

from .models import franquicia

class franquiciaadmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion','activo')
	list_filter = ['activo']

admin.site.register(franquicia,franquiciaadmin)
