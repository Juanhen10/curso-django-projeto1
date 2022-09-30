from django.shortcuts import render
from utils.jogos.factory import make_jogos

from jogos.models import Jogos


def home(request):
    jogos = Jogos.objects.all().order_by('-id')
    return render(request, 'jogos/pages/home.html', context={
        'jogos': jogos,
    })


def category(request, category_id):
    jogos = Jogos.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'jogos/pages/home.html', context={
        'jogos': jogos,
    })



def jogos(request, id):
    return render(request, 'jogos/pages/jogos-view.html', context={
        'jogos': make_jogos(),
        'is_datail_page': True,
    })
