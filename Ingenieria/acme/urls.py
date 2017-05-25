from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), #se asigna view llamada post_list al url ^$
    url(r'^login/', views.login, name='login'),  # se asigna view llamada post_list al url ^$
    url(r'^signup/', views.signup, name='signup'),
    url(r'^gestion/', views.gestion, name='gestion'),
]