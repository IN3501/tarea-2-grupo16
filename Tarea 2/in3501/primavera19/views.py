from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'home.html')

def inputs(request):
	return render(request, 'inputs.html')


def recuperar(request):
	Nombre=request.POST["inputText"]
	Edad=request.POST["inputNumber"]
	Correo=request.POST["inputEmail"]
	Departamento=request.POST["input Select"]
	Tema=request.POST["exampleRadios"]
	l_var=request.POST.getlist('check[]')
	

	diccionario={}
	diccionario["Nombre"]=Nombre
	diccionario["Edad"]=Edad
	diccionario["Correo"]=Correo
	diccionario["Departamento"]=Departamento
	diccionario["Tema"]=Tema
	diccionario["Alimento"]=l_var

	return render(request, "mostrar_resultado.html", diccionario)

