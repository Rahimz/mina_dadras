from django.contrib import admin

from .models import About, Social


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'image',]


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    
    
