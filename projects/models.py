from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    
    # Imágenes (Usaremos Cloudinary más adelante, por ahora ImageField estándar)
    image = models.ImageField(upload_to='projects/images/', verbose_name="Imagen Principal")
    image_tablet = models.ImageField(upload_to='projects/images/tablet/', blank=True, null=True, verbose_name="Imagen Tablet")
    image_mobile = models.ImageField(upload_to='projects/images/mobile/', blank=True, null=True, verbose_name="Imagen Móvil")
    
    # Links
    url_site = models.URLField(blank=True, null=True, verbose_name="Sitio Web")
    url_repository = models.URLField(blank=True, null=True, verbose_name="Repositorio GitHub")
    
    # Relación ManyToMany con Skills (lo definiremos en el paso siguiente, pero lo dejamos listo)
    skills = models.ManyToManyField('skills.Skill', related_name='projects', blank=True, verbose_name="Tecnologías")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created_at'] # Ordenar por el más nuevo primero

    def __str__(self):
        return self.title
