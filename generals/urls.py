from django.urls import path

from . import views


app_name = 'generals'

urlpatterns = [
    path('about/', views.AboutView, name='about'),
    path('', views.HomeView, name='home'),
]
