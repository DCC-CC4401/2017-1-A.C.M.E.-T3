# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf

from datetime import datetime, date, time, timedelta
import calendar

from django.urls import reverse

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
    usuarioFijo = VendedorFijoProfile.objects.filter(user=user)
    if usuarioFijo:
        disponibilidad = timeDisp(usuarioFijo[0])
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
    if request.user.is_authenticated():
        client = ClientProfile.objects.get(user = request.user)
        favorito = client.favVendFijo.filter(user=User.objects.get(username=usuario))
        if favorito:
            fav = True
        if not favorito:
            fav = False
        return render(request, 'acme/perfilvendedorsimple.html',
                      {'users': users, 'productos': productos, 'disponibilidad': disponibilidad, 'fav': fav})
    return render(request, 'acme/perfilvendedorsimple.html',
                  {'users': users, 'productos': productos, 'disponibilidad': disponibilidad, 'fav': None})

def agregarfavoritoFijo(request, id_user):
    vendedor = VendedorFijoProfile.objects.filter(id=id_user)
    client = ClientProfile.objects.get(user=request.user)
    if vendedor:
        userfijo = vendedor[0]
        useramb = None
        userfijo.likes += 1
        print (userfijo.likes )
        userfijo.save()
        print (userfijo.likes)
        client.favVendFijo.add(vendedor[0])
        client.save()
        return render(request, 'acme/Favoritos.html',
                          {'userfijo': userfijo, 'useramb': useramb, 'full_name': userfijo.user.username})

def agregarfavoritoMovil(request, id_user):
    vendedorAmb = VendedorAmbProfile.objects.filter(id=id_user)
    client = ClientProfile.objects.get(user=request.user)
    if vendedorAmb:
        userfijo = None
        useramb = vendedorAmb[0]
        vendedorAmb[0].likes += 1
        vendedorAmb[0].save()
        client.favVendAmb.add(vendedorAmb[0])
        client.save()
        return render(request, 'acme/Favoritos.html',
                          {'userfijo': userfijo, 'useramb': useramb, 'full_name': useramb.user.username})

def eliminarfavoritoFijo(request, id_user):
    vendedor = VendedorFijoProfile.objects.filter(id=id_user)
    client = ClientProfile.objects.get(user=request.user)
    if vendedor :
        userfijo = vendedor[0]
        useramb = None
        vendedor[0].likes -= 1
        vendedor[0].save()
        client.favVendFijo.remove(vendedor[0])
        client.save()
        return render(request, 'acme/Favoritos-Elim.html',
                          {'userfijo': userfijo, 'useramb': useramb, 'full_name': userfijo.user.username})

def eliminarfavoritoMovil(request, id_user):
    vendedorAmb = VendedorAmbProfile.objects.filter(id=id_user)
    client = ClientProfile.objects.get(user=request.user)
    if vendedorAmb:
        userfijo = None
        useramb = vendedorAmb[0]
        vendedorAmb[0].likes -= 1
        vendedorAmb[0].save()
        client.favVendAmb.remove(vendedorAmb[0])
        client.save()
        return render(request, 'acme/Favoritos-Elim.html',
                          {'userfijo': userfijo, 'useramb': useramb, 'full_name': useramb.user.username})

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

def modificar(request, id_producto):

    p = Product.objects.get(pk=id_producto)

    if request.method == 'POST':
        if request.POST.get('type') == 'ELIMINAR':
            p.delete()
            return redirect('acme:perfil')

        p.name = request.POST.get('name', p.name)
        p.stock = request.POST.get('stock', p.stock)
        p.description = request.POST.get('description', p.description)
        p.cost = request.POST.get('cost', p.cost)
        p.category = request.POST.get('category', p.category)
        if request.FILES.__len__() != 0:
            p.photo = request.FILES.get('photo', None)
        p.save()
        return redirect('acme:index')

    else:
        form = ProductForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'acme/modificar-producto.html', {'producto':p})

def delete(request, id_producto):
    emp = Product.objects.get(pk=id_producto)
    if request.method == 'POST':
        emp.delete()
        return redirect('acme:index')
    return render(request, 'acme/eliminar-producto.html', {'producto': emp})

def delete_user(request, usuario):
    emp = User.objects.get(username=usuario.username)
    if request.method == 'POST':
        emp.delete()
        return redirect('acme:index')

def viewClientAmb(request, usuario):
    users = get_object_or_404(VendedorAmbProfile, user=User.objects.get(username=usuario))
    productos = Product.objects.filter(vendedor=User.objects.get(username=usuario))
    if request.user.is_authenticated():
        client = ClientProfile.objects.get(user=request.user)
        favorito = client.favVendAmb.filter(user=User.objects.get(username=usuario))
        if favorito:
            fav = True
        if not favorito:
            fav = False
        return render(request, 'acme/perfilvendedorsimple.html', {'users': users, 'productos': productos, 'fav': fav})
    return render(request, 'acme/perfilvendedorsimple.html', {'users': users, 'productos': productos, 'fav': None})

def editar(request):
    usuario = VendedorFijoProfile.objects.filter(user=request.user)
    if usuario:
        if request.method == 'GET':
            form = VendFijoForm(instance=usuario[0])
            form.initial['first_name'] = request.user.first_name
            form.initial['last_name'] = request.user.last_name
            form.initial['fijo'] = True

        else:
            us = usuario[0]
            if request.FILES.__len__() != 0:
                us.avatar = request.FILES.get('avatar')

            if request.POST.get('student') == 'on':
                us.student = True
            else:
                us.student = False

            if request.POST.get('cash') == 'on':
                us.cash = True
            else:
                us.cash = False

            if request.POST.get('debit') == 'on':
                us.debit = True
            else:
                us.debit = False

            if request.POST.get('credit') == 'on':
                us.credit = True
            else:
                us.credit = False

            us.end_time = request.POST.get('end_time')
            us.init_time = request.POST.get('init_time')

            update_profile(request)
            us.save()
            return redirect('acme:index')
    else:
        usuario = VendedorAmbProfile.objects.filter(user=request.user)
        if request.method == 'GET':
            form = VendAmbForm(instance=VendedorAmbProfile.objects.filter(user=request.user)[0])
            form.initial['first_name'] = request.user.first_name
            form.initial['last_name'] = request.user.last_name
            form.initial['fijo'] = False

        else:
            us = usuario[0]
            if request.FILES.__len__() != 0:
                us.avatar = request.FILES.get('avatar')

            if request.POST.get('student') == 'on':
                us.student = True
            else:
                us.student = False

            if request.POST.get('cash') == 'on':
                us.cash = True
            else:
                us.cash = False

            if request.POST.get('debit') == 'on':
                us.debit = True
            else:
                us.debit = False

            if request.POST.get('credit') == 'on':
                us.credit = True
            else:
                us.credit = False

            if request.POST.get('check') == 'on':
                us.check = True
            else:
                us.check = False

            update_profile(request)
            us.save()
            return redirect('acme:index')

    return render(request, 'acme/editar.html', {'form': form})

def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST)
        if form.is_valid():
            form.save(request.user)
    else:
        form = UpdateProfile()

    args['form'] = form





