from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    
    # Rutas relativas a la carpeta static (ej: "img/projects/desktop/proyecto1.webp")
    image_desktop = models.CharField(max_length=255, verbose_name="Static Path (Desktop)")
    image_tablet = models.CharField(max_length=255, blank=True, null=True, verbose_name="Static Path (Tablet)")
    image_mobile = models.CharField(max_length=255, blank=True, null=True, verbose_name="Static Path (Mobile)")
    
    # NUEVO CAMPO: Ícono opcional para el botón de enlace
    icon = models.CharField(max_length=255, blank=True, null=True, verbose_name="Static Path (Button Icon)", help_text="Ej: img/icons/cj.svg")
    
    url_site = models.URLField(blank=True, null=True, verbose_name="Website URL")
    url_repository = models.URLField(blank=True, null=True, verbose_name="Repository URL")
    
    skills = models.ManyToManyField('skills.Skill', related_name='projects', blank=True, verbose_name="Tech Stack")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
