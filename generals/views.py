from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.db.models import Prefetch, Count

from projects.models import Project
from .models import About, Social


def HomeView(request):
    url = 'generals/home.html'
        
    projects = Project.objects.all()

    context = dict(
        page_title=_("Home"),
        nav='home',
        projects=projects,
    )
    # if not request.user.is_authenticated:
    #     url = 'generals/construction.html'
    return render (
        request,
        url,
        context
    )


def AboutView(request):
    about = About.objects.all().last()
    socials = Social.objects.all()
    context = dict(
        page_title=_("About me"),
        nav='about',
        about=about,
        socials=socials
    )
    return render (
        request,
        'generals/about.html',
        context
    )
