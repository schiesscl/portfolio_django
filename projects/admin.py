from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Project

# Cambiamos admin.ModelAdmin por TranslationAdmin
@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    # Si ya tienes list_display u otras configuraciones, mantenlas
    list_display = ('title', 'created_at') # Ejemplo
    
    # Esto habilitará pestañas o entradas para cada idioma en el admin
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
