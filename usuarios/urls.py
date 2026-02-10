from django.urls import path
from . import views

app_name = "usuarios"
urlpatterns = [
    path('', views.usuarios, name="usuarios"),
    path('register/', views.cadastro, name="cadastro"),
#    path('new_user/', views.novo_usuario, name="novo_usuario"),
#    path('detail_user/', views.detalhar_usuario, name="detalhar_usuario"),
#    path('edit_user/', views.editar_usuario, name="editar_usuario"),
#    path('delete_user/', views.remover_usuario, name="remover_usuario"),
]