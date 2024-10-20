from django.shortcuts import render, get_object_or_404
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


def ProjectDetailsView(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = dict(
        page_title=_("projects"),
        nav='projects',
        project=project,
    )
    return render (
        request,
        'projects/project.html',
        context
    )