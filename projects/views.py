from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from .models import Project

def ProjectsView(request):
    projects = Project.objects.all()
    context = dict(
        page_title=_("projects"),
        nav='projects',
        projects=projects,
    )
    return render (
        request,
        'projects/projects.html',
        context
    )
