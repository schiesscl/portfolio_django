"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog

# Importamos la vista 'home' desde tu app 'projects'
from projects.views import home 

# URLs sin prefijo de idioma (para cambio de idioma y JS catalog)
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]

# URLs con prefijo de idioma (/en/, /es/)
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    
    # Ruta raíz ('') -> Ejecuta la vista 'home'
    path('', home, name='home'),
    
    prefix_default_language=False,  # No añade prefijo al idioma por defecto (inglés)
)

# Configuración especial para servir imágenes (Media) cuando estamos en modo DEBUG (Local)
# Esto es vital para ver las fotos en tu PC antes de subirlas a la nube
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

