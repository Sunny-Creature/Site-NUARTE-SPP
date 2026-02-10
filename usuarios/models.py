from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    icone_usuario = models.ImageField(upload_to="icones_usuarios", blank=True)

    # Define qual o campo é o nome de usuário
    USERNAME_FIELD = "username"
    # Necessário para createsuperuser continuar funcionando
    REQUIRED_FIELDS = ["username"]