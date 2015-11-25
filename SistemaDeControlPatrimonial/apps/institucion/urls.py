from django.conf.urls import *
from rest_framework import routers
import views

router = routers.DefaultRouter()
router.register(r'institucion',views.InstitucionViewSet)

urlpatterns = patterns('',
                       url(r'^institucion', 'SistemaDeControlPatrimonial.apps.institucion.views.intitucion'),
                       url(r'^api/',include(router.urls)),
                       )