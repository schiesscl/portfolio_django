from django.shortcuts import render
from .models import Project
from skills.models import Skill

def home(request):
    projects = list(Project.objects.all().order_by('created_at'))
    skills = Skill.objects.all().order_by('order')
    
    n_projects = len(projects)
    if n_projects > 3:
        # Ventana deslizante lineal sin wrap-around (ej. 1,2,3 luego 2,3,4)
        project_slides_desktop = [
            projects[i:i + 3] for i in range(n_projects - 2)
        ]
    else:
        project_slides_desktop = [projects]

    project_slides_mobile = [[p] for p in projects]
    
    return render(request, 'home.html', {
        'projects': projects,
        'project_slides_desktop': project_slides_desktop,
        'project_slides_mobile': project_slides_mobile,
        'skills': skills
    })
