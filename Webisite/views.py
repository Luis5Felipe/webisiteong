from django.shortcuts import render
from .models import MidiaEventos
from .models import Voluntario

# from .forms import VoluntarioForm

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



# def voluntario_view(request): 
#     if request.method == 'POST':
#         nome = request.POST.get('nome_Voluntario',None)
#         cpf = request.POST.get('cpf_Voluntario', None)
#         data = request.POST.get('data_Nascimento', None)
#         email = request.POST.get('email', None)
#         telefone = request.POST.get('telefone', None)
#         genero = request.POST.get('genero', None)
        
        
#     return render(request,'_layouts/volunario.html', )


def voluntario_view(request): 
    if request.method == 'POST':
        # Coleta os dados do formulário
        nome = request.POST.get('nome_Voluntario', None)
        cpf = request.POST.get('cpf_Voluntario', None)
        data = request.POST.get('data_Nascimento', None)
        email = request.POST.get('email', None)
        telefone = request.POST.get('telefone', None)
        genero = request.POST.get('genero', None)
        
        # Cria uma nova instância do modelo Voluntario
        voluntario = Voluntario(
            nome_Voluntario=nome,
            cpf_Voluntario=cpf,
            data_Nascimento=data,
            email=email,
            telefone=telefone,
            genero=genero
        )

        # Salva a instância no banco de dados
        voluntario.save()

        # Você pode adicionar uma mensagem de sucesso ou redirecionar para outra página
        success_message = "Cadastro realizado com sucesso!"
        return render(request, '_layouts/volunario.html', {'success_message': success_message})
    
    return render(request, '_layouts/volunario.html')





#  def clean(self):
#         # Valida o CPF do voluntário
#         if len(self.cpf_Voluntario) != 11 or not self.cpf_Voluntario.isdigit():
#             raise ValidationError("CPF do voluntário deve ter 11 dígitos numéricos.")
        
#         # Ou, se preferir usar a biblioteca CPF:
#         # cpf = CPF()
#         # if not cpf.validate(self.cpf_Voluntario):
#         #     raise ValidationError("CPF do voluntário inválido.")
        
#         # Valida a idade do voluntário
#         if self.data_Nascimento:
#             today = date.today()
#             idade_calculada = today.year - self.data_Nascimento.year - ((today.month, today.day) < (self.data_Nascimento.month, self.data_Nascimento.day))
            
#             if idade_calculada < 0:
#                 raise ValidationError("Idade inválida calculada para o voluntário.")
            
#             self.idade_Voluntario = idade_calculada