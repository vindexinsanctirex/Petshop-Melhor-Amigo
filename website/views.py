# website/views.py
from django.shortcuts import render

def home(request):
    context = {
        'titulo': 'Melhor Amigo',
        'slogan': 'Cuidando do seu melhor amigo como se fosse nosso'
    }
    return render(request, 'website/home.html', context)

def produtos(request):
    context = {
        'titulo': 'Nossos Produtos e Serviços',
    }
    return render(request, 'website/produtos.html', context)

def galeria(request):
    context = {
        'titulo': 'Galeria de Fotos',
    }
    return render(request, 'website/galeria.html', context)

def contato(request):
    context = {
        'titulo': 'Fale Conosco',
    }
    return render(request, 'website/contato.html', context)