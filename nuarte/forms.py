from django import forms

class FormContato(forms.Form):
    nome = forms.CharField(label="Nome:")
    mensagem = forms.CharField(widget=forms.Textarea, max_length="500", label="Mensagem:")