from django.views.generic import ListView
from models import franquicia

class HomeView(ListView):
        template_name = 'home.html'
	model = franquicia
	context_object_name = 'franquicias'
