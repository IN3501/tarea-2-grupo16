from django.urls import path
from .views import * 

urlpatterns = [
	path('', index, name ='index'),
	path('inputs/', inputs, name='inputs'),
	path("mostrar_resultado", recuperar, name='mostrar_resultado'),
	path('Contacto/', Contacto, name='Contacto'),
	path("mostrar_contacto", recuperar1, name='mostrar_contactos'),
	path("cierres", cierres, name='cierres'),
	path("cortinas", cortinas, name='cortinas'),
	path("productos", productos, name='productos'),
	path("creaciondecuenta", creaciondecuenta, name='creaciondecuenta'),
	path("iniciodesesion", iniciodesesion, name='iniciodesesion'),
	path("carritodecompras", carritodecompras,name='carritodecompras'),
	path("verificacioncrearusuario", recuperar2, name='verificacioncrearusuario'),
	path("mostrar_inicio", recuperar3, name='mostrar_inicio'),
]