from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.db.models import Prefetch

from projects.models import Attachement, Category


def HomeView(request):
    attachments = Attachement.objects.filter(cover=True)
    categories = Category.objects.filter(parent__isnull=True).prefetch_related(Prefetch('projects__attachments', queryset=attachments))
    context = dict(
        page_title=_("Home"),
        nav='home',
        # attachments=attachments,
        categories=categories,
    )
    return render (
        request,
        'generals/home.html',
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
