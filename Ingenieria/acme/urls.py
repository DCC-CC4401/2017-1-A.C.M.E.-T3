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
                  # url(r'^PerfilVendedor/(?P<vendedor>\S+)/$', views.perfilVendedor, name='perfilVendedor'),
                  # url(r'^eliminarfav/(?P<id>[0-9]+)/$', views.eliminarfavorito, name='addfav'),
                  # url(r'^agregarfav/(?P<id>[0-9]+)/$', views.agregarfavorito, name='deletefav'),
                  url(r'^gestion/$', views.gestion, name='gestion'),
                  url(r'^eliminar/(?P<id_producto>\d+)/$', views.delete, name='eliminar'),
                  url(r'^modificar/(?P<id_producto>\d+)/$', views.modificar, name='modificar'),
                  url(r'^editar/$', views.editar, name='modificar_perfil'),
                  url(r'^(?P<usuario>[a-zA-Z0-9_\-.:]+)/Perfil/$', views.viewClientFijo, name='ViewClient'),
                  url(r'^(?P<usuario>[a-zA-Z0-9_\-.:]+)/perfil/$', views.viewClientAmb, name='ViewClient2'),
                  # url(r'^Perfil/$', views.perfil, name='perfil'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
