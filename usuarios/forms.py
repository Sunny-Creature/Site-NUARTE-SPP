from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "email", "icone_usuario", "is_active", "last_login", "groups"]