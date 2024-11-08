from django.db import models
from django.core.exceptions import ValidationError
from validate_docbr import CPF
from datetime import date

#tabela paciente
class Paciente(models.Model):
    id_Paciente = models.CharField(max_length=20, primary_key=True)
    nome_Paciente = models.CharField(max_length=255)
    nome_Responsavel = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=255)
    cpf_responsavel = models.CharField(max_length=255)
    data_Nascimento = models.DateField()
    idade_Paciente = models.IntegerField()
    endereço = models.CharField(max_length=255)
    data_Registro = models.DateTimeField(auto_now_add=True)
    genero_list = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    ]
    genero = models.CharField(max_length=1, choices=genero_list, default='O')

    def __str__(self):
        return self.nome_Paciente
    
    def clean(self):
        cpf = CPF()
        if not cpf.validate(self.cpf_responsavel):
            raise ValidationError("CPF do responsável inválido")
        
    # Valida a idade do paciente
        if self.data_Nascimento:
            today = date.today()
            self.idade_Paciente = today.year - self.data_Nascimento.year - ((today.month, today.day) < (self.data_Nascimento.month, self.data_Nascimento.day))
        
        if self.idade_Paciente < 0:
            raise ValidationError("Idade inválida calculada para o paciente")
    # Antes de salvar, executa a validação
    def save(self, *args, **kwargs):
        self.clean()
        super(Paciente, self).save(*args, **kwargs)


#Tabela Voluntario
class Voluntario(models.Model):
    id_Voluntario = models.CharField(max_length=20, primary_key=True)
    nome_Voluntario = models.CharField(max_length=255)
    cpf_Voluntario = models.CharField(max_length=255)
    data_Nascimento = models.DateField()
    telefone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    endereço = models.CharField(max_length=255)
    data_Registro = models.DateTimeField(auto_now_add=True)
    idade_Voluntario = models.IntegerField()
    genero_list = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    ]
    genero = models.CharField(max_length=1, choices=genero_list, default='O')

    def __str__(self):
        return self.nome_Voluntario

    def clean(self):
        # Valida o CPF do voluntário
        cpf = CPF()  
        if not cpf.validate(self.cpf_Voluntario):
            raise ValidationError("CPF do voluntário inválido.")
        
        # Valida a idade do voluntário
        if self.data_Nascimento:
            today = date.today()
            idade_calculada = today.year - self.data_Nascimento.year - ((today.month, today.day) < (self.data_Nascimento.month, self.data_Nascimento.day))
            
            if idade_calculada < 0:
                raise ValidationError("Idade inválida calculada para o voluntário.")
            
            self.idade_Voluntario = idade_calculada
    
    # Antes de salvar, executa a validação
    def save(self, *args, **kwargs):
        self.clean()
        super(Voluntario, self).save(*args, **kwargs)


    
