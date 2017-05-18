from django.db import models
from thumbs import ImageWithThumbsField
# Create your models here.

class TipoPropiedad (models.Model):
	nombre = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre

class Localidad(models.Model):
	nombre = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre

class TipoOperacion(models.Model):
	nombre = models.CharField(max_length=20)

	def __unicode__(self):
		return self.nombre

class Propiedad(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.TextField()
	textoListado = models.TextField(default="vacio")
	codigo = models.CharField(max_length=40)
	tipoPropiedad = models.ForeignKey(TipoPropiedad)
	localidad = models.ForeignKey(Localidad)
	precio = models.TextField()
	superficieCubierta = models.CharField(max_length=20)
	superficieTotal = models.CharField(max_length=20)	
	tipoOperacion = models.ForeignKey(TipoOperacion)	
	habitaciones = models.CharField(max_length=20)
	banios = models.CharField(max_length=5)
	cocheras = models.TextField()
	geolocalizacion = models.TextField(null=True , blank=True)
	disponible = models.BooleanField() 
	estado = models.CharField(max_length=20)
	imagen1 = ImageWithThumbsField(upload_to='chalita', null=True , blank=True , default='chalita/defecto/images.jpeg' )
	imagen2 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen3 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen4 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen5 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen6 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen7 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen8 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen9 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen10 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen11 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen12 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen13 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen14 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen15 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen16 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen17 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen18 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen19 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen20 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen21 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen22 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen23 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen24 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )
	imagen25 = ImageWithThumbsField(upload_to='chalita',null=True , blank=True )