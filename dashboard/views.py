from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from nuarte.models import Coordenadores, Grupos, Eventos, Historia
from usuarios.models import Usuario

# Create your views here.

#@login_required
#@permission_required