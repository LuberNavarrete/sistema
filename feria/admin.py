from django.contrib import admin
from .models import franquicia,producto

class franquiciaadmin(admin.ModelAdmin):
	search_fields = ['nombre','descripcion']
	list_display = ('nombre','descripcion','activo')
	list_filter = ['activo']

class productoadmin(admin.ModelAdmin):
	search_fields = ['nombre','descripcion']
        list_display = ('franquicia','nombre','descripcion','activo')
        list_filter = ['activo']

admin.site.register(producto,productoadmin)
admin.site.register(franquicia,franquiciaadmin)
