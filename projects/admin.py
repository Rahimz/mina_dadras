from django.contrib import admin

from .models import Category, Project, Attachement

class AttachmentInline(admin.StackedInline):
    model = Attachement
    raw_id_fields = ('project',)    
    extra = 1   


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'active']
    inlines = [AttachmentInline,]


@admin.register(Attachement)
class AttachementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'project', 'attach_type', 'attachment_order', 'cover']
    list_editable =['cover', 'attachment_order']