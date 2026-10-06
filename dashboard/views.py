from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from nuarte.models import Coordenadores, Grupos, Eventos, Historia
from usuarios.models import Usuario
from nuarte.forms import FormContato

# Create your views here.

@login_required
def dashboard(request):
    context  ={
        "bolsista": Usuario.objects.first(),
    }
    if not request.user.has_perm("usuarios.adicionar_usuario"):
        return redirect("index")
    return render(request, "dashboard.html", context)

@login_required
def grupos(request):
    context = {
        ""
    }
    return render(request, "dashboard")