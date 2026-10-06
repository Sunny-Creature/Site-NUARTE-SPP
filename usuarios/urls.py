from django.urls import path
from . import views

app_name = "usuarios"
urlpatterns = [
    path('', views.usuarios, name="usuarios"),
    path('register/', views.cadastro, name="cadastro"),
#    path('novo_usuario/', views.novo_usuario, name="novo_usuario"),
#    path('detalhar_usuario/', views.detalhar_usuario, name="detalhar_usuario"),
#    path('editar_usuario/', views.editar_usuario, name="editar_usuario"),
#    path('remover_usuario/', views.remover_usuario, name="remover_usuario"),
]