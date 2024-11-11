from django.shortcuts import render
from .models import MidiaEventos
from .models import Voluntario
from .models import Paciente
from datetime import datetime , date
from django.core.exceptions import ValidationError
from validate_docbr import CPF
from django.contrib import messages 

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
        # Coletando os dados do formulário
        nome = request.POST.get('nome_Voluntario', None)
        cpf = request.POST.get('cpf_Voluntario', None)
        data = request.POST.get('data_Nascimento', None)
        email = request.POST.get('email', None)
        telefone = request.POST.get('telefone', None)
        genero = request.POST.get('genero', None)

        try:
            # Verificando se a data de nascimento foi informada e convertendo
            data_nascimento = datetime.strptime(data, '%Y-%m-%d').date() if data else None

            # Validando o CPF
            cpf_validator = CPF()
            if not cpf_validator.validate(cpf):
                raise ValidationError("CPF do voluntário inválido.")

            # Verificando a idade (opcional, se necessário calcular)
            if data_nascimento:
                today = datetime.today().date()
                idade_calculada = today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
                
                if idade_calculada < 18:
                    raise ValidationError("O voluntário deve ser maior de idade para se cadastrar.")
            
            # Criando a instância do modelo Voluntário
            voluntario = Voluntario(
                nome_Voluntario=nome,
                cpf_Voluntario=cpf,
                data_Nascimento=data_nascimento,
                email=email,
                telefone=telefone,
                genero=genero
            )
            voluntario.save()

            # Mensagem de sucesso
            messages.success(request, "Cadastro realizado com sucesso!")

        except ValidationError as e:
            # Mensagem de erro, caso algum dado não passe na validação
            messages.error(request, str(e))  # Exibindo a exceção de erro como mensagem

    return render(request, '_layouts/volunario.html')


def consulta_view(request):
    if request.method == 'POST':
        nome_res = request.POST.get('nome_responsavel', None)
        nome = request.POST.get('nome_paciente', None)
        cpf = request.POST.get('cpf_responsavel', None)
        data = request.POST.get('data_Nascimento', None)
        email = request.POST.get('email', None)
        telefone = request.POST.get('telefone', None)
        endereco = request.POST.get('endereco', None)
        genero = request.POST.get('genero', None)

        try:
            # Convertendo a data de nascimento
            data_nascimento = datetime.strptime(data, '%Y-%m-%d').date() if data else None

            if data_nascimento:
                today = date.today()
                idade_calculada = today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
                
                if idade_calculada < 0:
                    raise ValidationError("Idade inválida calculada para o voluntário.")
            else:
                idade_calculada = None 

            # Validando o CPF
            cpf_validator = CPF()
            if not cpf_validator.validate(cpf):
                raise ValidationError("CPF do voluntário inválido.")

            # Criando a instância do modelo Paciente
            paciente_instance = Paciente(
                nome_Responsavel=nome_res,
                nome_Paciente=nome,
                cpf_responsavel=cpf,
                data_Nascimento=data_nascimento,
                email=email,
                endereco=endereco,
                telefone=telefone,
                genero=genero,
                idade_Paciente=idade_calculada,
            )
            paciente_instance.save()

            # Mensagem de sucesso
            messages.success(request, "Cadastro realizado com sucesso!")

        except ValidationError as e:
            # Mensagem de erro
            messages.error(request, str(e))  # Passando a exceção como mensagem de erro

    return render(request, '_layouts/consulta.html')









