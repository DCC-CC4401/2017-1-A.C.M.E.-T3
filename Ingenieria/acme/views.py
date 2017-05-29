# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from datetime import datetime, date, time, timedelta
import calendar
from acme.forms import UserForm, VendFijoForm, VendAmbForm
from acme.models import *

def vendedor(request):
    return render(request, 'acme/vendedor-profile-page.html', {})

def indexNotRegister(request):
    userfijo = VendedorFijoProfile.objects.all()
    useramb = VendedorAmbProfile.objects.all()
    if request.user.is_authenticated():
        if ClientProfile.objects.filter(user=request.user):
            ambFav = ClientProfile.objects.get(user=request.user).favVendAmb.all()
            fijoFav = ClientProfile.objects.get(user=request.user).favVendFijo.all()
            if ambFav:
                ambFav = ambFav[0]
                if userfijo:
                    print "hola"
                    userfijo = userfijo[0]
                if useramb:
                    useramb = None
            if fijoFav:
                fijoFav = fijoFav[0]
                if userfijo:
                    userfijo = None
                if useramb:
                    useramb = useramb[0]
            if not fijoFav and not ambFav:
                if userfijo:
                    userfijo = userfijo[0]
                if useramb:
                    useramb = useramb[0]
            return render(request, 'acme/init.html', {'usersfijo': userfijo, 'useramb': useramb, 'ambFav': ambFav, 'fijoFav': fijoFav})
    if userfijo:
        userfijo = userfijo[0]
    if useramb:
        useramb = useramb[0]
    return render(request, 'acme/init.html', {'usersfijo': userfijo, 'useramb': useramb}) #va a construir lo puesto en la planilla .html senhalada

def register(request):
    return render(request, 'acme/loggedin.html',{})

def signup(request):
    return render(request, 'acme/profile.html', {})

def signupClient(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('acme:Register')
    else:
        form = UserForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/signupCliente.html', args)

def signupVendAmb(request):
    if request.method == 'POST':
        form = VendAmbForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('acme:Register')
    else:
        form = VendAmbForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/signupVendAmb.html', args)

def signupVendFijo(request):
    if request.method == 'POST':
        form = VendFijoForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('acme:Register')
    else:
        form = VendFijoForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/signupVendFijo.html', args)

def viewClientFijo(request, usuario):
    #users = get_object_or_404(VendedorFijoProfile, username = usuario)
    #print users
    return render(request, 'acme/profile.html', {})# {'users':users})

def viewClientAmb(request, usuario):
    #query_result_amb = VendedorAmbProfile.objects.all()
    return render(request, 'acme/profile.html', {})# {'users':users})

def perfil(request):

    user= request.user
    productos= Product.objects.filter(vendedor=user)
    print (productos)

    usuarioFijo = VendedorFijoProfile.objects.filter(user=user)
    if (usuarioFijo.__len__() !=0):
        ahora = datetime.now()
        tiempoInicial = usuarioFijo[0].init_time.__str__().split(":")
        tiempoFinal= usuarioFijo[0].end_time.__str__().split(":")
        horaInicial=time(int(tiempoInicial[0]),int(tiempoInicial[1]),int(tiempoInicial[2]))
        horaFinal = time(int(tiempoFinal[0]),int(tiempoFinal[1]),int(tiempoFinal[2]))
        horaActual= time(ahora.hour,ahora.minute,ahora.second)
        if horaInicial <= horaActual and horaActual <= horaFinal :
            return render(request, 'acme/vendedor-profile-page.html', {'productos': productos , 'disponibilidad':"Disponible"})
        else:
            return render(request, 'acme/vendedor-profile-page.html', {'productos': productos, 'disponibilidad': "No Disponible"})

    return render(request, 'acme/vendedor-profile-page.html',{'productos':productos})
