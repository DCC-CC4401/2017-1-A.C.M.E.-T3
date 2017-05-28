# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf

from acme.forms import UserForm, VendFijoForm, VendAmbForm
from acme.models import VendedorAmbProfile


def indexNotRegister(request):
    return render(request, 'acme/init.html', {}) #va a construir lo puesto en la planilla .html senhalada

#def indexRegister(request):
#    return render(request, 'acme/../loginApp/templates/loginApp/init_register.html', {}) #va a construir lo puesto en la planilla .html senhalada

def register(request):
    return render(request, 'acme/loggedin.html',{})

#def login(request):
#    return render(request, 'acme/login.html', {}) #va a construir lo puesto en la planilla .html senhalada

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