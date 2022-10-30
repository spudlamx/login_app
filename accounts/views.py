
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Accounts

# Create your views here.

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['user']
    y = request.POST['pass']

    account = Accounts(username=x, password=y)
    account.save()
    return HttpResponseRedirect(reverse('home'))

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def account(request):
    x = request.POST['user']
    y = request.POST['pass']

    if Accounts.objects.filter(username=x, password=y).exists():
        template = loader.get_template('account.html')
    else:
        template = loader.get_template('not_auth.html')
    return HttpResponse(template.render({}, request))

def back_home(request):
    return HttpResponseRedirect(reverse('home'))

def back_login(request):
    return HttpResponseRedirect(reverse('login'))