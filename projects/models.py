from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid 
from django.urls import reverse

from tools.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(
        _("Name"),
        max_length=150,
    )
    slug = models.SlugField(
        _("Slug"),
        allow_unicode=True,
    )
    parent = models.ForeignKey(
        'self',
        verbose_name=_("Parent category"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("projects:category_details", kwargs={"slug": self.slug})
    

class Project(TimeStampedModel):
    class Type(models.TextChoices):
        IMAGE = 'image', _("Image gallery")
        MIX = 'mix', _("Mix content")
        
    title = models.CharField(
        _("Title"),
        max_length=150,
    )
    slug = models.SlugField(
        _("Slug"),
        allow_unicode=True,
    )
    type = models.CharField(
        _("Type"),
        max_length=10,
        default=Type.IMAGE,
        choices=Type.choices,
    )
    uuid = models.UUIDField(
        default=uuid.uuid4, 
        editable=False,
        unique=True
    )
    category = models.ForeignKey(
        Category,
        verbose_name=_("Category"),
        related_name='projects',
        on_delete=models.PROTECT,        
    )
    

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects") 

    def __str__(self):
        return self.title

    def get_cover_attachment(self):
        return self.attachments.all().filter(cover=True, attach_type=Attachement.AttachType.IMAGE).last() or None
    
    def get_absolute_url(self):
        return reverse("projects:project_details", kwargs={"slug": self.slug})

class Attachement(TimeStampedModel):    
    class AttachType(models.TextChoices):
        TITLE =  'title', _("Title")
        TEXT =  'text', _("Text")
        PDF = 'PDF', _("PDF")
        DOCS = 'DOCS', _("DOCS")
        IMAGE = 'image', _("Image")
        LINK = 'link', _("Link")
        VIDEOFILE = 'video_file', _("Video file")   
        SCRIPT = 'script', _("Script")
    
    project = models.ForeignKey(
        Project,
        verbose_name=_("Project"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="attachments"
    )
    title = models.CharField(
        _("Title"),
        max_length=250,
    )
    cover = models.BooleanField(
        _("Cover image"),
        default=False,
    )
    uuid = models.UUIDField(
        default=uuid.uuid4, 
        editable=False,
        unique=True
    )
    attach_type = models.CharField(
        max_length=15,
        default=AttachType.PDF,
        choices=AttachType.choices
    )
    text = models.TextField(
        _("Text"),        
        blank=True,
        null=True
    )
    file = models.FileField(
        _("File"),
        upload_to='projects/attachs/',
        blank=True, 
        null=True,
    )
    image_alt = models.CharField(
        _("Image alt"),
        max_length=150,
        null=True,
        blank=True
    )
    url = models.URLField(
        _("Link"),
        null=True,
        blank=True,
    )
    script = models.TextField(
        _("Script"),
        null=True,
        blank=True
    )
    attachment_order = models.PositiveSmallIntegerField(
        _("Attachment order"),
        default=1,
    )   
    
    
    active = models.BooleanField(
        _("Active"),
        default=True
    )
    
    class Meta:
        ordering = ('attachment_order',)      
        verbose_name = _("Attachment")
        verbose_name_plural = _("Attachments")

    def __str__(self):
        return self.title    
   
    # def save(self, *args, **kwargs):        
    #     return super().save(*args, **kwargs)
