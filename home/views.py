from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting


# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'home'}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def kisiler(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'kisiler'}
    return render(request, 'kisiler.html', context)

def iletisim(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'iletisim'}
    return render(request, 'iletisim.html', context)

def profil(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'profil'}
    return render(request, 'profil.html', context)


def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')

    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'profil'}
    return render(request, 'login.html', context)
