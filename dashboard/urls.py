from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    # -- EVENTOS --
    path('', views.dashboard, name="dashboard"),
#    path('eventos/new', views.evento_novo, name="evento_novo"),
#    path('eventos/<int:id_event>/detail', views.eventos_detalhar, name="evento_detalhar"),
#    path('eventos/<int:id_event>/edit', views.eventos_editar, name="eventos_editar"),
#    path('eventos/<int:id_evento>/remove/', views.eventos_remover, name="eventos_remover"),

    # -- HISTORIA --
#    path('historia/edit', views.historia, name="historia_editar"),

    # -- GRUPOS --
#    path('', views.grupos),
#    path('', views.grupos),
]