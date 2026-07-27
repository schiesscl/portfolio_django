from django.shortcuts import render
from .models import Project
from skills.models import Skill

def home(request):
    projects = list(Project.objects.all().order_by('created_at'))
    skills = Skill.objects.all().order_by('order')
    
    # Agrupar proyectos para carrusel responsivo
    project_slides_desktop = [projects[i:i + 3] for i in range(0, len(projects), 3)]
    project_slides_mobile = [[p] for p in projects]
    
    return render(request, 'home.html', {
        'projects': projects,
        'project_slides_desktop': project_slides_desktop,
        'project_slides_mobile': project_slides_mobile,
        'skills': skills
    })
