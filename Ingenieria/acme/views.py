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

from acme.forms import UserForm, VendFijoForm


def index(request):
    return render(request, 'acme/init.html', {}) #va a construir lo puesto en la planilla .html senhalada

def login(request):
    return render(request, 'acme/login.html', {}) #va a construir lo puesto en la planilla .html senhalada

#def signup(request):
#    return render(request, 'acme/signup.html', {}) #va a construir lo puesto en la planilla .html senhalada

def signup(request):
    return render(request, 'acme/profile.html', {})

def signupClient(request):
    print request.method
    if request.method == 'POST':
        form = UserForm(request.POST)
        print form.is_valid()
        print form.errors
        #profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():# and profile_form.is_valid():
            form.save()
            HttpResponseRedirect('/accounts/loggedin/')
            #profile_form.save()
            #messages.success(request, ('Your profile was successfully updated!'))
            #return redirect('settings:profile')
    else:
        print "no"
        form = UserForm()
        #profile_form = ProfileForm(instance=request.user.profile)
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/signupCliente.html', args)

def signupVendAmb(request):
    print request.method
    if request.method == 'POST':
        form = UserForm(request.POST)
        print form.is_valid()
        print form.errors
        #profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():# and profile_form.is_valid():
            form.save()
            HttpResponseRedirect('/accounts/loggedin/')
            #profile_form.save()
            #messages.success(request, ('Your profile was successfully updated!'))
            #return redirect('settings:profile')
    else:
        print "no"
        form = UserForm()
        #profile_form = ProfileForm(instance=request.user.profile)
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/signupVendAmb.html', args)

def signupVendFijo(request):
    print request.method
    if request.method == 'POST':
        form = VendFijoForm(request.POST)
        print form.is_valid()
        print form.errors
        if form.is_valid():# and profile_form.is_valid():
            form.save()
            HttpResponseRedirect('/accounts/loggedin/')
            #profile_form.save()
            #messages.success(request, ('Your profile was successfully updated!'))
            #return redirect('settings:profile')
    else:
        print "no"
        form = VendFijoForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/signupVendFijo.html', args)