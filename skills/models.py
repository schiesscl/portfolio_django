from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    logo = models.ImageField(upload_to='skills/images/', verbose_name="Logo")
    version = models.CharField(max_length=50, blank=True, null=True, verbose_name="Versión (Opcional)")
    
    # Orden personalizado para que puedas decidir cuál sale primero
    order = models.IntegerField(default=0, verbose_name="Orden de aparición")

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['order', 'name'] # Ordenar por tu número manual, luego alfabético

    def __str__(self):
        return self.name
