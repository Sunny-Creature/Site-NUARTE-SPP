from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('events/', views.eventos, name="eventos"),
    path('groups/', views.grupos, name="grupos"),
    path('history/', views.historia, name="historia"),
]