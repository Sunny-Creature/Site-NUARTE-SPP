from django.contrib import admin

# Register your models here.
from .models import Grupos, Coordenadores, Eventos, Historia

admin.site.register(Grupos)
admin.site.register(Coordenadores)
admin.site.register(Eventos)
admin.site.register(Historia)