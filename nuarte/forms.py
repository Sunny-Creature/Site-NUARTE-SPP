from django import forms

class FormContato(forms.form):
    nome = forms.CharField(label="Nome:")
    email = forms.EmailField(label="E-mail:")
    mensagem = forms.CharField(widget=forms.Textarea, max_lenght="250", label="Mensagem:")