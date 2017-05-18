from django.shortcuts import render, render_to_response, redirect, RequestContext
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from django.views.decorators.csrf import csrf_protect
from forms import *
from models import *
# Create your views here.


def Buscador (request):	
	if request.method == 'POST':
		form1=filtroForm()
		tiposOp = str(request.POST['Tipo_de_Operacion'])
		tiposProp = str(request.POST['Tipo_de_Propiedad'])
       	localidad = str(request.POST['Localidad'])
        propiedades = Propiedad.objects.filter(localidad__pk__icontains=localidad,tipoPropiedad__pk__icontains=tiposProp).filter(tipoOperacion__pk__icontains=tiposOp)
        return render(request,'listaPropiedades.html',locals())

def Turismo (request):
	return render(request,'turismo.html',locals())


def Index (request):
	form=filtroForm()
	ultimas = Propiedad.objects.order_by('?')[:4]
	return render(request,'index.html',locals())

def Contacto (request):
	if request.method == "POST":
		form2 = contactoForm (request.POST)
		if form2.is_valid():
			n = form2.cleaned_data['nombre']
    		c = form2.cleaned_data['consulta']
    		e = form2.cleaned_data['email']
    		f = form2.cleaned_data['telefono']
    		consul= 'Nombre: '+n+ '\n'+'Email: '+e+'\n'+'Consulta: '+c+ '\n'+'Telefono: '+f
    		send_mail(n, consul, e ,['chalitacriniganpropiedades@gmail.com'], fail_silently=False)	
		return HttpResponseRedirect("/")
	else:
		form2 = contactoForm ()		
	return render(request,'contactoForm.html',locals())
#	form2 = contactoForm ()
#	if request.method == "POST":
#		form2 = contactoForm (request.POST)
#		if form2.is_valid():
#			n = form2.cleaned_data['nombre']
  #  		c = form2.cleaned_data['consulta']
  #  		e = form2.cleaned_data['email']
   # 		consul= n+ '\n'+e+'\n'+c+'\n'+resultado.codigo 
  #  		send_mail(n, consul, e ,['llanitos.serviciosinformaticos@gmail.com'], fail_silently=True)	
#		return HttpResponseRedirect("/")	
#	return render(request,'contactoForm.html',locals())

@csrf_protect
def PropiedadSimple (request, id):	
	resultado = Propiedad.objects.get(pk=id)
	if request.method == "POST":
		form = contactoForm(request.POST)
		if form.is_valid():
			n = form.cleaned_data['nombre']
    		c = form.cleaned_data['consulta']
    		e = form.cleaned_data['email']
    		f = form.cleaned_data['telefono']
    		consul= 'Nombre: '+n+ '\n'+'Email: '+e+'\n'+'Consulta: '+c+'\n'+'Telefono: '+f+'\n'+'Codigo: '+resultado.codigo

    		send_mail(n, consul, e ,['chalitacriniganpropiedades@gmail.com'], fail_silently=True)	
		return HttpResponseRedirect("/")
	form2 = contactoForm ()		
	return render(request,'1propiedad_simple.html',locals())

@csrf_protect
def PropiedadSimpleLlamado (request):	
	if request.method == "POST":
		form1 = llamadoForm(request.POST)
		if form1.is_valid():
			n = form.cleaned_data['nombre']
    		c = form.cleaned_data['telefono']    		
    		consul= 'Nombre: '+n+ '\n'+'Telefono: '+c+'\n'+'Codigo: '+resultado.codigo  
    		send_mail(n, consul, c ,['chalitacriniganpropiedades@gmail.com'], fail_silently=True)	
		return HttpResponseRedirect("/")
	form3 = llamadoForm ()		
	return render(request,'1propiedad_simple.html',locals())

def BuscadorVenta (request):
	form1=filtroForm()
	propiedades = Propiedad.objects.filter(tipoOperacion__pk = str(1))
	return render(request,'listaPropiedades.html',locals())

def BuscadorAlquiPerman (request):
	form1=filtroForm()
	propiedades = Propiedad.objects.filter(tipoOperacion__pk = str(3))
	return render(request,'listaPropiedades.html',locals())	

def BuscadorAlquiTemp (request):
	form1=filtroForm()
	propiedades = Propiedad.objects.filter(tipoOperacion__pk = str(2))
	return render(request,'listaPropiedades.html',locals())
