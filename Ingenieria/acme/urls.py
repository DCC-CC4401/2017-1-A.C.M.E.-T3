from django.conf.urls import url

from . import views



urlpatterns = [
    url(r'^$', views.indexNotRegister, name='index'),
    url(r'^signup-successful/', views.register, name='Register'),
    url(r'index/', views.indexRegister, name='indexRegister'),
    url(r'^login/', views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^signup-Client/', views.signupClient, name='signupCliente'),
    url(r'^signup-Vendedor-Fijo/', views.signupVendFijo, name='signupFijo'),
    url(r'^signup-Vendedor-Ambulante/', views.signupVendAmb, name='signupAmb'),
]