from django.shortcuts import render
from .models import MidiaEventos



def home_view(request):
    eventos = MidiaEventos.objects.order_by('-data_evento')
    return render(request,'_layouts/home.html', {'eventos': eventos})

# def eventos_list(request):
#     # Recupera todos os objetos de MidiaEventos
#     eventos = MidiaEventos.objects.all()
    
#     # Envia os eventos para o template
#     return render(request, '_layouts/home.html', {'eventos': eventos})
