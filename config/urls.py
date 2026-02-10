"""
URL configuration for config project.
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include("nuarte.urls")),
    path('dashboard/', include("dashboard.urls")),
    path('usuarios/', include("usuarios.urls")),
    path('admin/', admin.site.urls),
    
    # URLs de autenticação com namespace 'registro'
    path('registro/', include(([
        path('login/', auth_views.LoginView.as_view(template_name='registro/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registro/password_change.html'), name='password_change'),
        path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registro/password_change_done.html'), name='password_change_done'),
    ], 'registro'), namespace='registro')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
