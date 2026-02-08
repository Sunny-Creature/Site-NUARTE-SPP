from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    icone_usuario = models.ImageField()
    nome_usuario = models.CharField(max_length="50", unique=True)