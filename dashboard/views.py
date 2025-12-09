from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from nuarte.models import Grupos, Orientadores, Eventos, Historia
from dashboard.models import UserLogin

# Create your views here.

@login_required
def dashboard(request):
    context = {
        "user_login": UserLogin.objects.all(),
    }
    return render(request, 'dashboard/dashboard.html', context)