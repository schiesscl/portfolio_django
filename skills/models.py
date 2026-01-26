from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    
    # Ruta relativa (ej: "img/logos/java.svg")
    logo = models.CharField(max_length=255, verbose_name="Static Path (Logo)")
    
    version = models.CharField(max_length=50, blank=True, null=True, verbose_name="Version")
    order = models.IntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
