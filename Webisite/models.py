from django.db import models
from django.core.exceptions import ValidationError
from validate_docbr import CPF
# Create your models here.
# Create your models here.


class Voluntario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False,
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        null=False,
        blank=False
    )
    telefone = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.nome

    def clean(self):
        cpf = CPF()
        if not cpf.validate(self.cpf):
            raise ValidationError("CPF inválido")


class Paciente(models.Model):
    nome_paciente = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    nome_responsavel = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    cpf_responsavel = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=255,
        null=False,
        blank=False
    )
    idade = models.IntegerField(
        null=False,
        blank=False
    )
    telefone = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )
    voluntario = models.ForeignKey(
        Voluntario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome_paciente

    def clean(self):
        cpf = CPF()
        if not cpf.validate(self.cpf_responsavel):
            raise ValidationError("CPF do responsável inválido")


class Visita(models.Model):
    nome = models.EmailField(
        max_length=255,
        null=True,
        blank=False
    )
    email = models.EmailField(
        max_length=255,
        null=False,
        blank=False
    )
    telefone = models.CharField(
        max_length=11,
        null=False,
        blank=False
    )
    horario = models.TimeField(
        null=False,
        blank=False
    )
    motivo = models.CharField(
        max_length=500,
        null=False,
        blank=False
    )
    voluntario = models.ForeignKey(
        Voluntario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Visita de {self.usuario.nome} às {self.horario}"