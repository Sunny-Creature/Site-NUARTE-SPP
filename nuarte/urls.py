from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('eventos/', views.eventos, name="eventos"),
    path('grupos/', views.grupos, name="grupos"),
    path('historia/', views.historia, name="historia"),
]