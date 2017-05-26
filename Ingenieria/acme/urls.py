from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^$', views.indexNotRegister, name='index'), #se asigna view llamada post_list al url ^$
    url(r'^signup-successful/', views.register, name='Register'),  # se asigna view llamada post_list al url ^$
    #url(r'^signup/', RegistroUsuario.as_view(), name='signup'),
    url(r'index/', views.indexRegister, name='indexRegister'),  # se asigna view llamada post_list al url ^$
    url(r'^login/', views.login, name='login'),  # se asigna view llamada post_list al url ^$
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signup-Client/', views.signupClient, name='signupCliente'),
    url(r'^signup-Vendedor-Fijo/', views.signupVendFijo, name='signupFijo'),
    url(r'^signup-Vendedor-Ambulante/', views.signupVendAmb, name='signupAmb'),
]