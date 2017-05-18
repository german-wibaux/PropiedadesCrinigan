#-*- coding: utf8 -*-
from django import forms
from django.forms import ModelForm
from models import *



class filtroForm (forms.Form):
	Tipo_de_Operacion = forms.ModelChoiceField(queryset=TipoOperacion.objects.all())
	Tipo_de_Propiedad = forms.ModelChoiceField(queryset=TipoPropiedad.objects.all())
	Localidad = forms.ModelChoiceField(queryset=Localidad.objects.all())

class contactoForm (forms.Form):
	nombre = forms.CharField()	
	email = forms.CharField()
	telefono = forms.CharField(required=False)
	consulta = forms.CharField(widget=forms.Textarea)
	

class llamadoForm (forms.Form):	
	nombre = forms.CharField()
	telefono = forms.CharField()


	
	