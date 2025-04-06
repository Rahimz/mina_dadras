from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.db.models import Prefetch, Count

from .models import Attachement, Category, Project

def ProjectsView(request):
    url = 'projects/projects.html'
    
    attachments = Attachement.objects.filter(cover=True)
    categories = (
        Category.objects
        .filter(parent__isnull=True)
        .annotate(project_count=Count('projects'))
        .filter(project_count__gt=0)
        .prefetch_related(Prefetch('projects__attachments', queryset=attachments))
    ) 
    
    context = dict(
        page_title=_("projects"),
        nav='projects',
        categories=categories,
    )
    # if not request.user.is_authenticated:
    #     url = 'generals/construction.html'
    return render (
        request,
        url,
        context
    )


def ProjectDetailsView(request, slug):
    project = get_object_or_404(Project, slug=slug)
    
    context = dict(
        page_title=_("Projects"),
        nav='projects',
        project=project,
    )
    return render (
        request,
        'projects/project.html',
        context
    )

def ProjectCategoriesView(request, slug):
    category = Category.objects.filter(slug=slug, project__active=True)
    
    context = dict(
        page_title=_("Category"),
        nav='projects',
        categories=category,
    )
    return render (
        request,
        'projects/projects.html',
        context
    )