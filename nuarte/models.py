from django.db import models

# Create your models here.

# - - - página principal - - -
class PagPrincipal(models.Model):
    img_principal = models.ImageField(upload_to="pag_principal/")

class Grupos(models.Model):
    nome_grupo = models.CharField(max_length=20)
    icone_grupo = models.ImageField(upload_to="icones_grupos/")

class Orientadores(models.Model):
    nome_orientador = models.CharField(max_length=40)
    icone_orientador = models.ImageField(upload_to="icones_orientadores/")

# - - - página de eventos - - -
class Eventos(models.Model):
    nome_evento = models.CharField(max_length=60)
    img_evento = models.ImageField(upload_to="img_eventos/")
    desc_evento = models.CharField(max_length=500)

# - - - página de história - - -
class Historia(models.Model):
    img_historia = models.ImageField(upload_to="img_historia/")
    descricao = models.CharField(max_length=500)