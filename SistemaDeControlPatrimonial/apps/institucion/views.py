from django.shortcuts import render, render_to_response, RequestContext
from serializers import InstitucionSerializer
from models import Institucion
from permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

def intitucion(request):
    instituciones = Institucion.objects.all()
    cntxt = {'instituciones':instituciones}
    return render(request,'institucion.html',cntxt)

class InstitucionViewSet(viewsets.ModelViewSet):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.user = self.request.user