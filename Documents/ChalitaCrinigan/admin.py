from django.contrib import admin
from models import *

# Register your models here.
class PropiedadAdmin (admin.ModelAdmin):
	list_display=('nombre', 'descripcion' ,'codigo','tipoPropiedad' , 'localidad' , 'precio' , 'superficieTotal', 'superficieCubierta' , 'tipoOperacion' , 'habitaciones' , 'banios','cocheras','geolocalizacion','estado','imagen1','imagen2','imagen3','imagen4','imagen5','imagen6','imagen7','imagen8','imagen9','imagen10','imagen11','imagen12','imagen13','imagen14','imagen15','imagen16','imagen17','imagen18','imagen19','imagen20','imagen21','imagen22','imagen23','imagen24','imagen25')

admin.site.register(Propiedad,PropiedadAdmin)

class TipoPropiedadAdmin (admin.ModelAdmin):
	list_display=('nombre', 'pk')

admin.site.register(TipoPropiedad,TipoPropiedadAdmin)

class TipoOperacionAdmin (admin.ModelAdmin):
	list_display=('nombre', 'pk')

admin.site.register(TipoOperacion,TipoOperacionAdmin)

class LocalidadAdmin (admin.ModelAdmin):
	list_display=('nombre',)

admin.site.register(Localidad,LocalidadAdmin)