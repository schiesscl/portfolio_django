from modeltranslation.translator import register, TranslationOptions
from .models import Project

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    # Lista los campos que necesitan traducción
    fields = ('title', 'description') 