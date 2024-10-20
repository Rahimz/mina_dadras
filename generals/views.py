from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def HomeView(request):
    context = dict(
        page_title=_("Home"),
        nav='home'
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
