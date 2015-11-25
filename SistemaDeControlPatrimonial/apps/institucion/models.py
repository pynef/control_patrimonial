from django.db import models
from django.contrib.auth.models import User

class Ubigeo(models.Model):
    departamento = models.CharField(max_length=2)
    distrito = models.CharField(max_length=2)
    provincia = models.CharField(max_length=2)
    nombre = models.CharField(max_length=64)

    def __str__(self):
        return '{0}'.format(self.nombre,self.departamento)

    class Meta:
        managed = True
        db_table = 'Ubigeo'



"""Empresa"""
class Institucion(models.Model):
    nombre = models.CharField(max_length=64)
    razon_social = models.CharField(max_length=128)
    direccion_fiscal = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    ruc = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,blank=True, null=True)
    workstation_name = models.CharField(max_length=64,blank=True, null=True)
    workstation_ip = models.CharField(max_length=64,blank=True, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.nombre,self.ruc)

    class Meta:
        managed = True
        db_table = 'Institucion'


class Sede(models.Model):
    institucion_id = models.ForeignKey(Institucion)
    nombre = models.CharField(max_length=64)
    ubicacion = models.CharField(max_length=6)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,blank=True, null=True)
    workstation_name = models.CharField(max_length=64,blank=True, null=True)
    workstation_ip = models.CharField(max_length=64,blank=True, null=True)

    def __str__(self):
        return '{0} - {1}'.format(self.institucion_id.nombre,self.nombre)

    class Meta:
        managed = True
        db_table = 'Sede'


class Local(models.Model):
    institucion_id = models.ForeignKey(Institucion)
    sede_id = models.ForeignKey(Sede)
    nombre = models.CharField(max_length=64)
    ubicacion = models.CharField(max_length=6)
    direccion = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,blank=True, null=True)
    workstation_name = models.CharField(max_length=64,blank=True, null=True)
    workstation_ip = models.CharField(max_length=64,blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'Local'


class Ambiente(models.Model):
    institucion_id = models.ForeignKey(Institucion)
    sede_id = models.ForeignKey(Sede)
    local_id = models.ForeignKey(Local)
    piso = models.IntegerField()
    nombre = models.CharField(max_length=64)
    capacidad = models.IntegerField()
    capacidad_adicional = models.IntegerField()
    observacion = models.TextField(blank=True, null=True)
    is_aula = models.NullBooleanField()
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,blank=True, null=True)
    workstation_name = models.CharField(max_length=64,blank=True, null=True)
    workstation_ip = models.CharField(max_length=64,blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'Ambiente'