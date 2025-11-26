from django.shortcuts import render
from .models import Grupos
from .models import Orientadores
from .forms import FormContato

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
            print("Salvo com sucesso!")

        context['form_contato'] = form

    return render(request, "nuarte/index.html", context)