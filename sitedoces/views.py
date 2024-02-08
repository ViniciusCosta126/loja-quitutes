from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, template_name='home/home.html')


def produtos(request):
    return render(request, template_name='produtos/produtos.html')


def produto_categoria(request, categoria_id):
    return HttpResponse(f'{categoria_id}')


def sobre(request):
    return render(request, template_name='sobre/sobre.html')


def contato(request):
    return render(request, template_name='contato/contato.html')
