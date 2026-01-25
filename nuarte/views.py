from django.shortcuts import render
from nuarte.models import Eventos, Grupos, Historia, Coordenadores
from nuarte.forms import FormContato

# Create your views here.

def index(request):
    context = {
        'grupos': Grupos.objects.all(),
        'coordenadores': Coordenadores.objects.all(),
        'form_contato': FormContato(),
    }

    if request.method == 'POST':
        form_contato = FormContato(request.POST)
        print("É um POST!")

        if form_contato.is_valid():
            form_contato.save()
            print("A mensagem foi salva com sucesso!")

        context['form_contato'] = form_contato
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
        'coordenadores': Coordenadores.objects.all(),
    }
    return render(request, "nuarte/historia.html", context)