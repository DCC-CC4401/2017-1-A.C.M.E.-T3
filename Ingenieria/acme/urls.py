from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #se asigna view llamada post_list al url ^$
    #url(r'^login/', LoginUsuario.as_view(), name='login'),  # se asigna view llamada post_list al url ^$
    #url(r'^signup/', RegistroUsuario.as_view(), name='signup'),
    url(r'^login/', views.login, name='login'),  # se asigna view llamada post_list al url ^$
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signup-Client/', views.signupClient, name='signupCliente'),
    url(r'^signup-Vendedor-Fijo/', views.signupVendFijo, name='signupFijo'),
    url(r'^signup-Vendedor-Ambulante/', views.signupVendAmb, name='signupAmb'),
]