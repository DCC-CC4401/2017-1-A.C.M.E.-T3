from django.contrib import auth
from django.shortcuts import render_to_response, redirect, render
from django.template.context_processors import csrf

from acme.models import *


def indexRegister(request):
    userfijo = VendedorFijoProfile.objects.all()
    useramb = VendedorAmbProfile.objects.all()
    print request
    if userfijo:
        userfijo = VendedorFijoProfile.objects.all()[0]
    if useramb:
        useramb = VendedorAmbProfile.objects.all()[0]
    return render(request, 'acme/initRegister.html', {'usersfijo': userfijo, 'useramb': useramb}) #va a construir lo puesto en la planilla .html senhalada

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('acme/login.html',c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect('log')
    else:
        return redirect('invalid_login')

def log(request):
    if request.user.first_name == '' or request.user.last_name == '':
        full_name = request.user.username
    else:
        full_name = request.user.get_full_name()
    return render_to_response('acme/log.html',{'full_name': full_name})

def invalid_login(request):
    return render_to_response('acme/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('acme/logout.html')

