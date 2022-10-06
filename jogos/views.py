import imp
from pickle import TRUE
from telnetlib import STATUS

from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.jogos.factory import make_jogos

from jogos.models import Jogos


def home(request):
    jogos = Jogos.objects.filter(is_published = True).order_by('-id')
    return render(request, 'jogos/pages/home.html', context={
        'jogos': jogos,
    })


def category(request, category_id):
    jogos = get_list_or_404(Jogos.objects.filter(category__id=category_id, 
    is_published=True,
    ).order_by('-id'))
    
    
    return render(request, 'jogos/pages/category.html', context={
        'jogos': jogos,
        'title':f'{jogos[0].category.name} - Categoy',
    })



def jogos(request, id):
    jogo = Jogos.objects.filter(
        pk=id,
        is_published=True,
    ).order_by('-id').first()

    jogo = get_object_or_404(Jogos, pk=id, is_published=True)

    return render(request, 'jogos/pages/jogos-view.html', context={
        'jogos': jogo,
        'is_datail_page': True,
    })
