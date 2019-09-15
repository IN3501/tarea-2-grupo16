from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('inputs/', inputs, name='inputs'),
	path("mostrar_resultado", recuperar, name='mostrar_resultado'),
	path('Contacto/', Contacto, name='Contacto'),
	path("mostrar_contacto", recuperar1, name='mostrar_contactos'),
	
]