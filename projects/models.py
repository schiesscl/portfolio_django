from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    
    # Imágenes Responsivas (Manual upload)
    image_desktop = models.ImageField(upload_to='projects/images/desktop/', verbose_name="Desktop Image")
    image_tablet = models.ImageField(upload_to='projects/images/tablet/', blank=True, null=True, verbose_name="Tablet Image")
    image_mobile = models.ImageField(upload_to='projects/images/mobile/', blank=True, null=True, verbose_name="Mobile Image")
    
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
