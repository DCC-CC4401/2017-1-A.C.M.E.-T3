# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf

from datetime import datetime, date, time, timedelta
import calendar

from acme.forms import *
from acme.models import *


## funcion auxiliar encargada de calcular disponibilidad del vendedor fijo

def timeDisp(usuario):
    ahora = datetime.now()
    tiempoInicial = usuario.init_time.__str__().split(":")
    tiempoFinal = usuario.end_time.__str__().split(":")
    horaInicial = time(int(tiempoInicial[0]), int(tiempoInicial[1]), int(tiempoInicial[2]))
    horaFinal = time(int(tiempoFinal[0]), int(tiempoFinal[1]), int(tiempoFinal[2]))
    horaActual = time(ahora.hour, ahora.minute, ahora.second)
    if horaInicial <= horaFinal:
        if horaInicial <= horaActual and horaActual <= horaFinal:
            return "Disponible"
        else:
            return "No Disponible"
    else:
        if horaInicial <= horaActual and horaFinal <= horaActual:
            return "Disponible"
        else:
            return "No Disponible"


def perfil(request):
    user = request.user
    productos = Product.objects.filter(vendedor=user)
    usuarioFijo = VendedorFijoProfile.objects.get(user=user)
    if usuarioFijo:
        disponibilidad = timeDisp(usuarioFijo)
        return render(request, 'acme/vendedor-profile-page.html',
                      {'productos': productos, 'disponibilidad': disponibilidad})
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
    return render(request, 'acme/signupVendFijo.html', args)


def gestion(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save()
            f.vendedor = request.user
            f.save()
            return redirect('acme:index')

    else:
        form = ProductForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/gestion-productos.html', args)


def viewClientFijo(request, usuario):
    users = VendedorFijoProfile.objects.get(user=User.objects.get(username=usuario))
    productos = Product.objects.filter(vendedor=User.objects.get(username=usuario))
    disponibilidad = timeDisp(users)
    return render(request, 'acme/perfilvendedorsimple.html',
                  {'users': users, 'productos': productos, 'disponibilidad': disponibilidad})


def agregarfavorito(request, id_user):
    vendedor = VendedorFijoProfile.objects.get(id=id_user)
    client = ClientProfile.objects.get(user=request.user)
    if vendedor != None:
        userfijo = vendedor
        useramb = None
        vendedor.likes += 1
        vendedor.save()
        client.favVendFijo.add(vendedor)
        client.save()
        return render(request, 'acme/Favoritos.html',
                      {'userfijo': userfijo, 'useramb': useramb, 'full_name': userfijo.user.username})
    else:
        vendedor = VendedorAmbProfile.objects.get(user=User.objects.get(id=id_user))
        userfijo = None
        useramb = vendedor
        vendedor.likes += 1
        vendedor.save()
        client.favVendAmb.add(vendedor)
        client.save()
        return render(request, 'acme/Favoritos.html',
                      {'userfijo': userfijo, 'useramb': useramb, 'full_name': userfijo.user.username})


def update(request, id):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        f = form.save()
        f.vendedor = request.user
        f.save()
        return redirect('acme:index')
    else:
        form = ProductForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return HttpResponse('update')


def delete(request, id_producto):
    emp = Product.objects.get(pk=id_producto)
    if request.method == 'POST':
        emp.delete()
        return redirect('acme:index')
    return render(request, 'acme/eliminar-producto.html', {'producto': emp})


def modificar(request, id_producto):
    p = Product.objects.get(id=id_producto)
    if request.method == 'GET':
        form = ProductForm(instance=p)
    else:
        form = ProductForm(request.POST, instance=p)
        if form.is_valid():
            f = form.save()
            f.vendedor = request.user
            f.save()
            delete(request, id_producto)
            return redirect('acme:index')
    return render(request, 'acme/modificar-producto.html', {'form': form})


def delete_user(request, usuario):
    emp = User.objects.get(username=usuario.username)
    if request.method == 'POST':
        emp.delete()
        return redirect('acme:index')


def editar(request):
    usuario = VendedorFijoProfile.objects.filter(user=request.user)
    if usuario:
        if request.method == 'GET':
            form = VendFijoForm(instance=usuario[0])
        else:
            form = VendFijoForm(request.POST, instance=usuario[0])
            if form.is_valid():
                user = form.save()
                user.save()
                delete_user(request, usuario[0])
                return redirect('acme:index')
    else:
        usuario = VendedorAmbProfile.objects.filter(user=request.user)
        if request.method == 'GET':
            form = VendAmbForm(instance=usuario[0])
        else:
            form = VendAmbForm(request.POST, instance=usuario[0])
            if form.is_valid():
                user = form.save()
                user.save()
                delete_user(request, usuario[0])
                return redirect('acme:index')
    return render(request, 'acme/editar.html', {'form': form})


def viewClientAmb(request, usuario):
    users = get_object_or_404(VendedorAmbProfile, user=User.objects.get(username=usuario))
    productos = Product.objects.filter(vendedor=User.objects.get(username=usuario))
    return render(request, 'acme/perfilvendedorsimple.html', {'users': users, 'productos': productos})
