from django.db import models

# Create your models here.
class UserLogin(models.Model):
    nome = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
#    senha = models.CharField(widget=forms.PasswordInput)