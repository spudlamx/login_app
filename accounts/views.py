
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Accounts

# Create your views here.

def home(request):
    # Sends the home template
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def add(request):
    # Sends the add template
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    # Gets username and password from user.
    x = request.POST['user']
    y = request.POST['pass']

    # adds username and password to database.
    account = Accounts(username=x, password=y)
    account.save()
    return HttpResponseRedirect(reverse('home'))

def login(request):
    # Sends the login template
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def account(request):
    # Gets username and password from user.
    x = request.POST['user']
    y = request.POST['pass']

    # Checks if username and password are in account table.
    # If it is, sends the account template. If not sends the not_auth template.
    if Accounts.objects.filter(username=x, password=y).exists():
        template = loader.get_template('account.html')
    else:
        template = loader.get_template('not_auth.html')
    return HttpResponse(template.render({}, request))

def back_home(request):
    # Returns to home page
    return HttpResponseRedirect(reverse('home'))

def back_login(request):
    # Returns to login page
    return HttpResponseRedirect(reverse('login'))