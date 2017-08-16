from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('campos/index.html')
    context={}
    return HttpResponse(template.render(context, request))

def guardarIndex(request):
    template = loader.get_template('campos/secundaria.html')
    user = request.POST.get('user_name')
    password = request.POST.get('user_password')
    context={
    'user': user,
    'password': password
    }
    return HttpResponse(template.render(context, request))

def secundaria(request):
    template = loader.get_template('campos/final.html')
    user = request.POST.get('user')
    password = request.POST.get('password')
    valor1 = request.POST.get('user_valor1')
    valor2 = request.POST.get('user_valor2')
    context={
    'user': user,
    'password': password,
    'valor1':valor1,
    'valor2':valor2
    }
    return HttpResponse(template.render(context, request))
