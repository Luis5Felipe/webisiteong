from django.contrib import admin
from Webisite.models import Voluntario
from Webisite.models import Paciente
from Webisite.models import Visita
# Register your models here.

class VoluntariosAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf','email','telefone')
    search_fields = ('nome',)

admin.site.register(Voluntario, VoluntariosAdmin)

class PacientesAdmin(admin.ModelAdmin):
    list_display = ('nome_paciente','nome_responsavel','cpf_responsavel','email','idade','telefone','voluntario')
    search_fields = ('nome_paciente', 'nome_responsavel','cpf_responsavel',)


admin.site.register(Paciente, PacientesAdmin)

class VisitasAdmin(admin.ModelAdmin):
    list_display = ('nome','email','telefone','horario')
    search_fields = ('nome','telefone')

admin.site.register(Visita, VisitasAdmin)