from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  url(r'^$', views.indexNotRegister, name='index'),
                  url(r'^signup-successful/$', views.register, name='Register'),
                  url(r'^signup/$', views.signup, name='signup'),
                  url(r'^signup-Client/$', views.signupClient, name='signupCliente'),
                  url(r'^signup-Vendedor-Fijo/$', views.signupVendFijo, name='signupFijo'),
                  url(r'^signup-Vendedor-Ambulante/$', views.signupVendAmb, name='signupAmb'),
                  url(r'^eliminarfav/ambulante/(?P<id_user>[a-zA-Z0-9_\-.:]+)/$', views.eliminarfavoritoMovil, name='favorito-elim_M'),
                  url(r'^eliminarfav/fijo/(?P<id_user>[a-zA-Z0-9_\-.:]+)/$', views.eliminarfavoritoFijo, name='favorito-elim_F'),
                  url(r'^favorito/ambulante/(?P<id_user>[a-zA-Z0-9_\-.:]+)/$', views.agregarfavoritoMovil, name='favorito_M'),
                  url(r'^favorito/fijo/(?P<id_user>[a-zA-Z0-9_\-.:]+)/$', views.agregarfavoritoFijo, name='favorito_F'),
                  url(r'^gestion/$', views.gestion, name='gestion'),
                  url(r'^eliminar/(?P<id_producto>\d+)/$', views.delete, name='eliminar'),
                  url(r'^modificar/(?P<id_producto>\d+)/$', views.modificar, name='modificar'),
                  url(r'^editar/$', views.editar, name='modificar_perfil'),
                  url(r'^(?P<usuario>[a-zA-Z0-9_\-.:]+)/Perfil/$', views.viewClientFijo, name='ViewClient'),
                  url(r'^(?P<usuario>[a-zA-Z0-9_\-.:]+)/perfil/$', views.viewClientAmb, name='ViewClient2'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
