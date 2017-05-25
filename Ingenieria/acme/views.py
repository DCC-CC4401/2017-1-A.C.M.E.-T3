# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'acme/init.html', {}) #va a construir lo puesto en la planilla .html senhalada

def login(request):
    return render(request, 'acme/login.html', {}) #va a construir lo puesto en la planilla .html senhalada

def signup(request):
    return render(request, 'acme/signup.html', {}) #va a construir lo puesto en la planilla .html senhalada

def gestion(request):
    return render(request, 'acme/gestion-productos.html', {})