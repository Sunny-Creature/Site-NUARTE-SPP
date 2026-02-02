from django.db import models

# Create your models here.

class Coordenadores(models.Model):
    nome_coordenador = models.CharField(max_length=100)
    bio_coordenador = models.CharField(max_length=200)
    icone_coordenador = models.ImageField(upload_to="icones_coordenadores/")

class Grupos(models.Model):
    nome_grupo = models.CharField(max_length=30)
    icone_grupo = models.ImageField(upload_to="icones_grupos/")
    nome_bolsista = models.CharField(max_length=100, null=True)
    icone_bolsista = models.ImageField(upload_to="icones_bolsistas/", null=True)

class Eventos(models.Model):
    titulo_evento = models.CharField(max_length=60)
    img_evento = models.ImageField(upload_to="img_eventos/")
    desc_evento = models.CharField(max_length=500)

class Historia(models.Model):
    img_historia = models.ImageField(upload_to="img_historia/")
    desc_historia = models.CharField(max_length=500)

# -- model para form de contato
class Contato(models.Model):
    nome_contato = models.CharField(max_length=100)
    mensagem_contato = models.CharField(max_length=250)
    data_envio_contato = models.DateField(auto_now_add=True)
    horas_envio_contato = models.TimeField(auto_now_add=True)