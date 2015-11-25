from rest_framework import serializers
from models import Institucion

class InstitucionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institucion
        fields = ('id','nombre','razon_social','direccion_fiscal','email','ruc')