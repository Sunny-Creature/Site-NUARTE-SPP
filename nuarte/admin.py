from django.contrib import admin

# Register your models here.
from .models import Grupos, Orientadores, Eventos, Historia

admin.site.register(Grupos)
admin.site.register(Orientadores)
admin.site.register(Eventos)
admin.site.register(Historia)