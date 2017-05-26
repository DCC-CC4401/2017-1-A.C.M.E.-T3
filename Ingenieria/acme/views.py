# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

#from acme.forms import UserForm, UserProfileForm
#from acme.models import UserProfile
from django.template.context_processors import csrf

from acme.forms import UserForm, VendFijoForm, VendAmbForm


def index(request):
    return render(request, 'acme/init.html', {}) #va a construir lo puesto en la planilla .html senhalada

def login(request):
    return render(request, 'acme/login.html', {}) #va a construir lo puesto en la planilla .html senhalada

#def signup(request):
#    return render(request, 'acme/signup.html', {}) #va a construir lo puesto en la planilla .html senhalada

def signup(request):
    return render(request, 'acme/profile.html', {})

def signupClient(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        print form.errors
        #profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():# and profile_form.is_valid():
            user = form.save()
            user.save()
            HttpResponseRedirect('/accounts/loggedin/')
            #profile_form.save()
            #messages.success(request, ('Your profile was successfully updated!'))
            #return redirect('settings:profile')
    else:
        form = UserForm()
        #profile_form = ProfileForm(instance=request.user.profile)
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/signupCliente.html', args)

def signupVendAmb(request):
    if request.method == 'POST':
        form = VendAmbForm(request.POST)
        print form.errors
        #profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():# and profile_form.is_valid():
            user = form.save()
            user.save()
            #HttpResponseRedirect('/accounts/loggedin/')
            #profile_form.save()
            #messages.success(request, ('Your profile was successfully updated!'))
            #return redirect('settings:profile')
    else:
        form = VendAmbForm()
        #profile_form = ProfileForm(instance=request.user.profile)
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/signupVendAmb.html', args)

def signupVendFijo(request):
    if request.method == 'POST':
        form = VendFijoForm(request.POST)
        print form.errors
        if form.is_valid():# and profile_form.is_valid():
            user = form.save()
            #HttpResponseRedirect('/accounts/loggedin/')
            #profile_form.save()
            user.save()
            messages.success(request, ('Your profile was successfully updated!'))
           #return redirect('acme/login.html')
    else:
        form = VendFijoForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/signupVendFijo.html', args)