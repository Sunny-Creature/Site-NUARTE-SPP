from django.db import models

# Create your models here.

class Grupos(models.Model):
    nome_grupo = models.CharField(max_length=20)
    icone_grupo = models.ImageField(upload_to="icones_grupos/")

class Orientadores(models.Model):
    nome_orientador = models.CharField(max_length=40)
    icone_orientador = models.ImageField(upload_to="icones_orientadores/")