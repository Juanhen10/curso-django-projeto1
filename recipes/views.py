import imp

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('HOME 1')


def contato(request):
    return HttpResponse('CONTATO 1')


def sobre(request):
    return HttpResponse('SOBRE')

