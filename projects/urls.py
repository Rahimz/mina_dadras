from django.urls import path 
from . import views 

app_name = 'projects'

urlpatterns = [
    path('<str:slug>/', views.ProjectDetailsView, name='project_details'),
    path('category/<str:slug>/', views.ProjectCategoriesView, name='category_details'),
    path('', views.ProjectsView, name='projects'),
]
