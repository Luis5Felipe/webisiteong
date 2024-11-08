from django.http import HttpResponseForbidden
from functools import wraps
from django.shortcuts import get_object_or_404
from .models import Voluntario

def voluntario_aprovado_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Supondo que você tenha uma relação entre o modelo de Usuário e Voluntário
        voluntario = get_object_or_404(Voluntario, user=request.user)
        
        # Verifica se o voluntário tem status 'aprovado'
        if voluntario.status != 'aprovado':
            return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
        
        # Se aprovado, executa a view
        return view_func(request, *args, **kwargs)

    return _wrapped_view
