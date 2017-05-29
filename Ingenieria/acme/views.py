# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf

from datetime import datetime, date, time, timedelta
import calendar

from acme.forms import UserForm, VendFijoForm, VendAmbForm
from acme.models import *


# def vendedor(request):
#    return render(request, 'acme/vendedor-profile-page.html', {})

def perfil(request):
    user = request.user
    productos = Product.objects.filter(vendedor=user)
    print (productos)

    usuarioFijo = VendedorFijoProfile.objects.filter(user=user)
    if (usuarioFijo.__len__() != 0):
        ahora = datetime.now()
        tiempoInicial = usuarioFijo[0].init_time.__str__().split(":")
        tiempoFinal = usuarioFijo[0].end_time.__str__().split(":")
        horaInicial = time(int(tiempoInicial[0]), int(tiempoInicial[1]), int(tiempoInicial[2]))
        horaFinal = time(int(tiempoFinal[0]), int(tiempoFinal[1]), int(tiempoFinal[2]))
        horaActual = time(ahora.hour, ahora.minute, ahora.second)
        if horaInicial <= horaFinal:
            if horaInicial <= horaActual and horaActual <= horaFinal:
                return render(request, 'acme/vendedor-profile-page.html',
                              {'productos': productos, 'disponibilidad': "Disponible"})
            else:
                return render(request, 'acme/vendedor-profile-page.html',
                              {'productos': productos, 'disponibilidad': "No Disponible"})
        else:
            if horaInicial <= horaActual and horaFinal <= horaActual:
                return render(request, 'acme/vendedor-profile-page.html',
                              {'productos': productos, 'disponibilidad': "Disponible"})
            else:
                return render(request, 'acme/vendedor-profile-page.html',
                              {'productos': productos, 'disponibilidad': "No Disponible"})
    return render(request, 'acme/vendedor-profile-page.html', {'productos': productos})


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
            return render(request, 'acme/init.html',
                          {'usersfijo': userfijo, 'useramb': useramb, 'ambFav': ambFav, 'fijoFav': fijoFav})
        else:
            return perfil(request)
    if userfijo:
        userfijo = userfijo[0]
    if useramb:
        useramb = useramb[0]
    return render(request, 'acme/init.html', {'usersfijo': userfijo,
                                              'useramb': useramb})  # va a construir lo puesto en la planilla .html senhalada


def register(request):
    return render(request, 'acme/loggedin.html', {})


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
    return render(request, 'acme/signupVendFijo.html')

def gestion(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            f.vendedor = request.user
            f.save()
            return redirect('acme:perfil')

    else:
        form = ProductForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/gestion-productos.html', args)


<<<<<<< HEAD
    user=request.user
    productos= Product.objects.filter(vendedor=user)
    print (productos)
=======
def viewClientFijo(request,usuario):
    users = VendedorFijoProfile.objects.get(user=User.objects.get(username=usuario))
    productos = Product.objects.filter(vendedor=User.objects.get(username=usuario))
    return render(request, 'acme/perfilvendedorsimple.html', {'users': users, 'productos': productos})
>>>>>>> origin/map


<<<<<<< HEAD
    return render(request, 'acme/vendedor-profile-page.html',{'productos':productos})


def perfilVendedor(request , vendedor):
    if request.user.is_authenticated():
        cliente = request.user
        usuarioVendedor = User.objects.filter(username=vendedor)
        vendedor = VendedorFijoProfile.objects.filter(user=usuarioVendedor[0])
        if vendedor.__len__() != 0 :
            ahora = datetime.now()
            tiempoInicial = vendedor[0].init_time.__str__().split(":")
            tiempoFinal = vendedor[0].end_time.__str__().split(":")
            horaInicial = time(int(tiempoInicial[0]), int(tiempoInicial[1]), int(tiempoInicial[2]))
            horaFinal = time(int(tiempoFinal[0]), int(tiempoFinal[1]), int(tiempoFinal[2]))
            horaActual = time(ahora.hour, ahora.minute, ahora.second)
            favoritos = ClientProfile.objects.filter(user=cliente,favVendFijo= vendedor[0])
            productos = Product.objects.filter(vendedor=vendedor[0].user)
            if favoritos.__len__()!=0 :
                if horaInicial <= horaActual and horaActual <= horaFinal:
                    return render(request, 'acme/perfilvendedorsimple.html',
                                  {'productos': productos, 'disponibilidad': "Disponible",'esfavorito': "true",'esAmbulante':None,'vendedor': vendedor[0]})
                else :
                    return render(request, 'acme/perfilvendedorsimple.html',
                                  {'productos': productos, 'disponibilidad': "No Disponible", 'esfavorito': "true",
                                   'esAmbulante': None,'vendedor': vendedor[0]})
            else :
                if horaInicial <= horaActual and horaActual <= horaFinal:
                    return render(request, 'acme/perfilvendedorsimple.html',
                                  {'productos': productos, 'disponibilidad': "Disponible", 'esfavorito': None,
                                   'esAmbulante': None,'vendedor': vendedor[0]})
                else:
                    return render(request, 'acme/perfilvendedorsimple.html',
                                  {'productos': productos, 'disponibilidad': "No Disponible", 'esfavorito': None,
                                   'esAmbulante': None,'vendedor': vendedor[0]})



        else:
            vendedor = VendedorAmbProfile.objects.filter(user=usuarioVendedor[0])
            favoritos = ClientProfile.objects.filter(user=cliente, favVendAmb=vendedor[0])
            productos = Product.objects.filter(vendedor=vendedor[0].user)
            if favoritos.__len__() != 0:
                    return render(request, 'acme/perfilvendedorsimple.html',
                                  {'productos': productos, 'esfavorito': "true",
                                   'esAmbulante': "true",'vendedor': vendedor[0]})

            else:
                    return render(request, 'acme/perfilvendedorsimple.html',
                                  {'productos': productos, 'esfavorito': None,
                                   'esAmbulante': "true",'vendedor': vendedor[0]})

    else :
        usuarioVendedor = User.objects.filter(username=vendedor)
        vendedor = VendedorFijoProfile.objects.filter(user=usuarioVendedor[0])
        if vendedor.__len__() != 0 :
            ahora = datetime.now()
            tiempoInicial = vendedor[0].init_time.__str__().split(":")
            tiempoFinal = vendedor[0].end_time.__str__().split(":")
            horaInicial = time(int(tiempoInicial[0]), int(tiempoInicial[1]), int(tiempoInicial[2]))
            horaFinal = time(int(tiempoFinal[0]), int(tiempoFinal[1]), int(tiempoFinal[2]))
            horaActual = time(ahora.hour, ahora.minute, ahora.second)
            productos = Product.objects.filter(vendedor=vendedor[0].user)
            if horaInicial <= horaActual and horaActual <= horaFinal:
                return render(request, 'acme/perfilvendedorsimple.html',
                              {'productos': productos, 'disponibilidad': "Disponible",
                               'esAmbulante': None, 'vendedor': vendedor[0]})
            else:
                return render(request, 'acme/perfilvendedorsimple.html',
                              {'productos': productos, 'disponibilidad': "No Disponible",
                               'esAmbulante': None, 'vendedor': vendedor[0]})
        else:
            vendedor = VendedorAmbProfile.objects.filter(user=usuarioVendedor[0])
            productos = Product.objects.filter(vendedor=vendedor[0].user)
            return render(request, 'acme/perfilvendedorsimple.html',
                          {'productos': productos,
                           'esAmbulante': "true", 'vendedor': vendedor[0]})

def agregarfavorito(request,id):
    vendedor =VendedorFijoProfile.objects.get(user= User.objects.get(id= id))
    if vendedor != None:
        vendedor.likes += 1
        vendedor.save()
        favoritismo = ClientProfile.objects.get(user=User.objects.get(username=request.user))
        relacion = ClientProfile(user=favoritismo.user, avatar=favoritismo.avatar, favVendFijo=vendedor)
        relacion.save()
    else:
        vendedor=VendedorAmbProfile.objects.get(user= User.objects.get(id= id))
        vendedor.likes += 1
        vendedor.save()
        favoritismo= ClientProfile.objects.get(user= User.objects.get(username = request.user) )
        relacion = ClientProfile(user=favoritismo.user,avatar=favoritismo.avatar,favVendAmb= vendedor)
        relacion.save()
    return render(request, 'acme/moficicacionFavoritos',
                  {})

def update(request, id):
    p = Product.objects.get(pk=id)
    #you can do this for as many fields as you like
    #here I asume you had a form with input like <input type="text" name="name"/>
    #so it's basically like that for all form fields
    p.name = request.POST.get('name')
    p.save()
    return HttpResponse('updated')

def delete(request, id):
    emp = Product.objects.get(pk=id)
    emp.delete()
    return HttpResponse('deleted')

def modificar(request):
    a=request.body
    return render(request, 'acme/modificar-producto.html', {})
=======
def viewClientAmb(request, usuario):
    users = get_object_or_404(VendedorAmbProfile, user= User.objects.get(username = usuario))
    productos = Product.objects.filter(vendedor=User.objects.get(username=usuario))
    return render(request, 'acme/perfilvendedorsimple.html',  {'users': users, 'productos': productos})
>>>>>>> origin/map
