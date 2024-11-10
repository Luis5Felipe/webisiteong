from django.shortcuts import render
from .models import MidiaEventos
#from .models import Voluntarios

def home_view(request):
    # Recuperar os 3 primeiros eventos, ordenados pela data (caso a data seja relevante para determinar a "mais antiga")
    eventos = MidiaEventos.objects.all().order_by('data_evento')[:3]

    if len(eventos) > 0:
        # Se já houver eventos, pegar o mais antigo
        evento_antigo = eventos[0]  # Evento mais antigo

        # Verifique se o novo evento foi enviado através do request (como um arquivo)
        if request.method == 'POST' and request.FILES.get('nova_imagem'):
            nova_imagem = request.FILES['nova_imagem']
            
            # Substituir a imagem do evento mais antigo
            evento_antigo.fotos = nova_imagem
            evento_antigo.save()  # Salvar a alteração no banco de dados

            # Atualizar a lista de eventos para refletir a alteração
            eventos = MidiaEventos.objects.all().order_by('data_evento')[:3]

    return render(request, '_layouts/home.html', {
        'evento1': eventos[0] if len(eventos) > 0 else None,
        'evento2': eventos[1] if len(eventos) > 1 else None,
        'evento3': eventos[2] if len(eventos) > 2 else None,
    })

def voluntario_view(request):
    # Aqui você pode passar qualquer contexto se necessário, mas no exemplo é vazio
    return render(request, '_layouts/volunario.html')