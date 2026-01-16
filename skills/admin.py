from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'order')
    list_editable = ('order',) # Permite cambiar el orden rápido desde la lista
