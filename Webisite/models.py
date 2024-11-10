from django.db import models
from django.core.exceptions import ValidationError
from validate_docbr import CPF
from datetime import date

#tabela paciente
class Paciente(models.Model):
    id_Paciente = models.AutoField(primary_key=True)
    nome_Paciente = models.CharField(max_length=255)
    nome_Responsavel = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=255)
    cpf_responsavel = models.CharField(max_length=255)
    data_Nascimento = models.DateField()
    idade_Paciente = models.IntegerField()
    endereco = models.CharField(max_length=255)
    data_Registro = models.DateTimeField(auto_now_add=True)
    genero_list = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    ]
    genero = models.CharField(max_length=1, choices=genero_list, default='O')
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
         ('rejeitado', 'Rejeitado'),
        ('concluído', 'Concluído'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    
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
    id_Voluntario = models.AutoField(primary_key=True)
    nome_Voluntario = models.CharField(max_length=255)
    cpf_Voluntario = models.CharField(max_length=11)  # Defina como 'max_length=11' para CPF com 11 caracteres
    data_Nascimento = models.DateField()
    telefone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    endereco = models.CharField(max_length=255)
    data_Registro = models.DateTimeField(auto_now_add=True)
    genero_list = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    ]
    genero = models.CharField(max_length=1, choices=genero_list, default='O')
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return self.nome_Voluntario

    
    def save(self, *args, **kwargs):
        self.clean()
        super(Voluntario, self).save(*args, **kwargs)
        
class Consulta(models.Model):
    data_Registro = models.DateTimeField(auto_now_add=True)
    id_Paciente_FK = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    id_Voluntario_FK = models.ForeignKey(Voluntario, on_delete=models.PROTECT)
    especialidade_list = [
        ('Psicologia Comportamental', 'Psicologia Comportamental'),
        ('Psicomotricidade', 'Psicomotricidade'),
        ('Fonoaudiologia', 'Fonoaudiologia'),
        ('Aplicadora em ABA', 'Aplicadora em ABA'),
        ('Estimulação Pedagógica', 'Estimulação Pedagógica'),
    ]
    especialidade = models.CharField(max_length=50, choices=especialidade_list, default='Psicologia Comportamental')
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('rejeitado', 'Rejeitado'),
        ('concluído', 'Concluído'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    def __str__(self):
        return f"Consulta de {self.id_Paciente_FK} com {self.id_Voluntario_FK} em {self.data_Registro}"
    

class MidiaEventos(models.Model):
    data_evento = models.DateField()
    fotos = models.ImageField(upload_to='eventos/',blank=True, null=True)
    
    def __str__(self):
        return f"Evento em {self.data_evento}"