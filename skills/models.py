from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    
    # Para skills, generalmente un solo logo vectorial (SVG o PNG transparente) basta para todos los tamaños.
    # Pero si quieres especificidad, puedes dejar los 3. Por simplicidad, empecemos con 1 logo principal.
    logo = models.ImageField(upload_to='skills/images/', verbose_name="Logo")
    
    version = models.CharField(max_length=50, blank=True, null=True, verbose_name="Version")
    order = models.IntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
