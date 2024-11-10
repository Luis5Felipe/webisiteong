# from django import forms
# from .models import Voluntario

# class VoluntarioForm(forms.ModelForm):
#     class Meta:
#         model = Voluntario
#         fields = ['nome_Voluntario', 'cpf_Voluntario', 'data_Nascimento', 'telefone', 'email', 'genero']

#     def clean_cpf_Voluntario(self):
#         cpf = self.cleaned_data.get('cpf_Voluntario')
#         if len(cpf) != 11 or not cpf.isdigit():
#             raise forms.ValidationError("CPF do voluntário deve ter 11 dígitos numéricos.")
#         # Você pode também usar uma biblioteca como `cpf` para validação mais rigorosa
#         return cpf

#     def clean_data_Nascimento(self):
#         data_nascimento = self.cleaned_data.get('data_Nascimento')
#         if data_nascimento:
#             today = date.today()
#             idade = today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
#             if idade < 0:
#                 raise forms.ValidationError("Idade inválida calculada para o voluntário.")
#         return data_nascimento