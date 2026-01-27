from django.shortcuts import render
from .models import Project
from skills.models import Skill

def home(request):
    projects = Project.objects.all().order_by('created_at')
    skills = Skill.objects.all().order_by('order')
    return render(request, 'home.html', {
        'projects': projects, 
        'skills': skills
    })
