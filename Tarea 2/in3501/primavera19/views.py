from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def inputs(request):
	return render(request, 'inputs.html')

def Contacto(request):
	return render(request, 'Contacto.html')

def iniciodesesion(request):
	return render(request, 'iniciodesesion.html')

def creaciondecuenta(request):
	return render(request, 'creaciondecuenta.html')


def recuperar(request):
	Nombre=request.POST["inputText"]
	Correo=request.POST["inputEmail"]
	Región=request.POST["inputSelect"]
	Ciudad=request.POST["inputCity"]
	Fecha=request.POST["inputDate"]
	Pedido=request.POST["textA"]
	Retiro=request.POST["exampleRadios"]

	diccionario={}
	diccionario["Nombre"]=Nombre
	diccionario["Correo"]=Correo
	diccionario["Región"]=Región
	diccionario["Ciudad"]=Ciudad
	diccionario["Fecha"]=Fecha
	diccionario["Pedido"]=Pedido
	diccionario["Retiro"]=Retiro

	return render(request, "mostrar_resultado.html", diccionario)

def recuperar1(request):
	nombre=request.POST["inputNombre"]
	telefono=request.POST["inputTelefono"]
	Email=request.POST["inputMail"]
	Asunto=request.POST["inputAsunto"]
	Mensaje=request.POST["inputMensaje"]

	diccionario={}
	diccionario["nombre"]=nombre
	diccionario["telefono"]=telefono
	diccionario["Email"]=Email
	diccionario["Asunto"]=Asunto
	diccionario["Mensaje"]=Mensaje

	return render(request, "mostrar_contacto.html", diccionario)

def cierres(request):
	return render(request, 'cierres.html')

def cortinas(request):
	return render(request, 'cortinas.html')

def productos(request):
	return render(request, 'productos.html')
	
def carritodecompras(request):
	return render(request,'carritodecompras.html')

def recuperar2(request):
	Nombre=request.POST["inputText"]
	
	diccionario={}
	diccionario["Nombre"]=Nombre

	return render(request, "verificacioncrearusuario.html", diccionario)