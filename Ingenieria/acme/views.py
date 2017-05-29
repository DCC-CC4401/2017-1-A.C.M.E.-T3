# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from datetime import datetime, date, time, timedelta
import calendar
from acme.forms import UserForm, VendFijoForm, VendAmbForm, ProductForm
from acme.models import Product, VendedorFijoProfile, ClientProfile


def vendedor(request):
    return render(request, 'acme/vendedor-profile-page.html', {})

def indexNotRegister(request):
    return render(request, 'acme/init.html', {}) #va a construir lo puesto en la planilla .html senhalada

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

def gestion(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            f.avatar = form.cleaned_data['avatar']
            f.vendedor = request.user
            f.save()
            return HttpResponse('image upload success')
    else:
        form = ProductForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/gestion-productos.html', args)

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
