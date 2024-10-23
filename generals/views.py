from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.db.models import Prefetch

from projects.models import Attachement, Category


def HomeView(request):
    url = 'generals/home.html'    

    attachments = Attachement.objects.filter(cover=True)
    categories = Category.objects.filter(parent__isnull=True).prefetch_related(Prefetch('projects__attachments', queryset=attachments))
    context = dict(
        page_title=_("Home"),
        nav='home',
        # attachments=attachments,
        categories=categories,
    )
    if not request.user.is_authenticated:
        url = 'generals/construction.html'
    return render (
        request,
        url,
        context
    )


def AboutView(request):
    context = dict(
        page_title=_("About me"),
        nav='about'
    )
    return render (
        request,
        'generals/about.html',
        context
    )
