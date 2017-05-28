#### VIEWS NEW
from django.contrib import auth
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('acme/login.html',c)

def auth_view(request):
    email = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=email,password=password)

    if user is not None:
        auth.login(request,user)
        return redirect('log')
    else:
        return redirect('invalid_login')

def log(request):
    return render_to_response('acme/log.html',{'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('acme/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('acme/logout.html')

### END