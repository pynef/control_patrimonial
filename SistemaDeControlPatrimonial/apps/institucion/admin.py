import socket
from django.contrib import admin
from SistemaDeControlPatrimonial.apps.institucion.models import Ubigeo
from SistemaDeControlPatrimonial.apps.institucion.models import Institucion
from SistemaDeControlPatrimonial.apps.institucion.models import Sede
from SistemaDeControlPatrimonial.apps.institucion.models import Local
from SistemaDeControlPatrimonial.apps.institucion.models import Ambiente



admin.site.register(Ubigeo)
admin.site.register(Institucion)
admin.site.register(Sede)
admin.site.register(Local)
admin.site.register(Ambiente)