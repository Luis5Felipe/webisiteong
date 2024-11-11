from django.shortcuts import render
from .models import MidiaEventos
from .models import Voluntario

def home_view(request):
    eventos = MidiaEventos.objects.all().order_by('data_evento')[:3]

    if len(eventos) > 0:
        evento_antigo = eventos[0]  
        if request.method == 'POST' and request.FILES.get('nova_imagem'):
            nova_imagem = request.FILES['nova_imagem']
            evento_antigo.fotos = nova_imagem
            evento_antigo.save()  
            eventos = MidiaEventos.objects.all().order_by('data_evento')[:3]

    return render(request, '_layouts/home.html', {
        'evento1': eventos[0] if len(eventos) > 0 else None,
        'evento2': eventos[1] if len(eventos) > 1 else None,
        'evento3': eventos[2] if len(eventos) > 2 else None,
    })


def voluntario_view(request): 
    if request.method == 'POST':
       
        nome = request.POST.get('nome_Voluntario', None)
        cpf = request.POST.get('cpf_Voluntario', None)
        data = request.POST.get('data_Nascimento', None)
        email = request.POST.get('email', None)
        telefone = request.POST.get('telefone', None)
        genero = request.POST.get('genero', None)
        
      
        voluntario = Voluntario(
            nome_Voluntario=nome,
            cpf_Voluntario=cpf,
            data_Nascimento=data,
            email=email,
            telefone=telefone,
            genero=genero
        )
        voluntario.save()
        success_message = "Cadastro realizado com sucesso!"
        return render(request, '_layouts/volunario.html', {'success_message': success_message})
    
    return render(request, '_layouts/volunario.html')

def consulta_view(request): 
#     if request.method == 'POST':
#         nome = request.POST.get('nome_Voluntario',None)
#         cpf = request.POST.get('cpf_Voluntario', None)
#         data = request.POST.get('data_Nascimento', None)
#         email = request.POST.get('email', None)
#         telefone = request.POST.get('telefone', None)
#         genero = request.POST.get('genero', None)
     return render(request,'_layouts/consulta.html', )











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