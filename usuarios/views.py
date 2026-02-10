from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Usuario
from .forms import UsuarioForm, UsuarioCreationForm
from nuarte.models import Coordenadores, Grupos, Historia, Eventos, Contato

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return
    else:
        form = UsuarioCreationForm()

    context = {
        "form": form,
    }
    return render(request, "usuarios/new_user.html", context)

@permission_required("usuarios.view_usuario", raise_exception=True)
def usuarios(request):
    context = {
        "usuarios": Usuario.objects.all(),
        "titulo_pagina": "NUARTE SPP - USUÁRIOS",
        "url_novo": "usuarios:usuarios_novo",
        "partial_tabela": "dashboard/partials/_tabela_usuarios.html",
    }
    return render(request, "dashboard/listar.html", context)