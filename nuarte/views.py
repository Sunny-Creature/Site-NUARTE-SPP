from django.shortcuts import render
from nuarte.models import Eventos, Grupos, Historia, Orientadores
from nuarte.forms import FormContato

# Create your views here.

def index(request):
    context = {
        'grupos': Grupos.objects.all(),
        'orientadores': Orientadores.objects.all(),
        'form_contato': FormContato(),
    }

    if request.method == 'POST':
        form = FormContato(request.POST)
        print("É um POST!")

        if form.is_valid():
            form.save()
            print("A mensagem foi enviada com sucesso!")

        context['form_contato'] = form
    return render(request, "nuarte/index.html", context)

def eventos(request):
    context = {
        'eventos': Eventos.objects.all(),
    }
    return render(request, "nuarte/eventos.html", context)

def grupos(request):
    context = {
        'grupos': Grupos.objects.all(),
    }
    return render(request, "nuarte/grupos.html", context)

def historia(request):
    context = {
        'historia': Historia.objects.all(),
    }
    return render(request, "nuarte/historia.html", context)