from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  url(r'^$', views.indexNotRegister, name='index'),
                  url(r'^signup-successful/$', views.register, name='Register'),
                  # url(r'^index/', views.indexRegister, name='indexRegister'),
                  #url(r'^login/$', views.login, name='login'),
                  url(r'^signup/$', views.signup, name='signup'),
                  url(r'^signup-Client/$', views.signupClient, name='signupCliente'),
                  url(r'^signup-Vendedor-Fijo/$', views.signupVendFijo, name='signupFijo'),
                  url(r'^signup-Vendedor-Ambulante/$', views.signupVendAmb, name='signupAmb'),
                  #url(r'^auth/$', views.auth_view, name='auth'),
                  #url(r'^logout/$', views.logout, name='logout'),
                  # {'next_page':  reverse_lazy('marcador_bookmark_list')}, name='acme_logout')
                  #url(r'^log/$', views.log, name='log'),
                  #url(r'^invalid_login/$', views.invalid_login,name='invalid_login'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
