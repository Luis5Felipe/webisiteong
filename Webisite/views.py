from django.shortcuts import render
from .models import MidiaEventos

def home_view(request):
    # Aqui, estamos pegando os 3 primeiros eventos como exemplo
    evento1 = MidiaEventos.objects.all()[0]
    evento2 = MidiaEventos.objects.all()[1]  # Segundo evento
    evento3 = MidiaEventos.objects.all()[2]  # Terceiro evento

    return render(request, '_layouts/home.html', {
        'evento1': evento1,
        'evento2': evento2,
        'evento3': evento3
    })

# def eventos_list(request):
#     # Recupera todos os objetos de MidiaEventos
#     eventos = MidiaEventos.objects.all()
    
#     # Envia os eventos para o template
#     return render(request, '_layouts/home.html', {'eventos': eventos})
