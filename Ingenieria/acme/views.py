# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from acme.forms import UserForm, VendFijoForm, VendAmbForm
from acme.models import *


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
