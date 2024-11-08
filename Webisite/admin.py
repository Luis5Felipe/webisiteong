from django.contrib import admin
from Webisite.models import Paciente
from Webisite.models import Voluntario
from Webisite.models import Consulta

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('status','nome_Paciente','nome_Responsavel','email','telefone','cpf_responsavel','data_Nascimento','idade_Paciente','endereco','data_Registro','genero')
    search_fields = ('id_Paciente','nome_Paciente')

class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ('status','nome_Voluntario','cpf_Voluntario','data_Nascimento','telefone','email','endereco','data_Registro','idade_Voluntario','genero')
    search_fields = ('nome_Voluntario','cpf_Voluntario')

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('status','data_Registro','id_Paciente_FK','id_Voluntario_FK','especialidade','data_Registro')
    search_fields = ('id_Paciente_FK','id_Voluntario_FK','data_Registro')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "id_Voluntario_FK":
            kwargs["queryset"] = Voluntario.objects.filter(status='aprovado')  # Somente voluntários aprovados
        elif db_field.name == "id_Paciente_FK":
            kwargs["queryset"] = Paciente.objects.filter(status='pendente')  # Somente pacientes com status 'ativo'
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Voluntario, VoluntarioAdmin)
admin.site.register(Consulta, ConsultaAdmin)