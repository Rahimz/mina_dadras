from django.db import models
from django.utils.translation import gettext_lazy as _

from tools.models import TimeStampedModel


class About(TimeStampedModel):
    image = models.ImageField(
        _("Image"),
        upload_to='about/'
    )
    home_page_image = models.ImageField(
        _("Image in home page"),
        upload_to='about/',
        null=True, 
        blank=True
    )
    title_about = models.CharField(
        max_length=150,
        null=True, blank=True,
    )
    about = models.TextField(
        _("About me")
    )
    cv_file = models.FileField(
        upload_to='about/',
        null=True,
        blank=True
    )
    cv_file_button = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    
    title_addition = models.CharField(
        _("Additional skils title"),
        max_length=150,
        null=True, blank=True,
    )
    addition = models.TextField(
        _("Additional skils"),
        blank=True
    )
    addition_image = models.ImageField(
        _("Addition image"),
        upload_to='about/',
        null=True,
        blank=True
    )
    addition_file = models.FileField(
        upload_to='about/',
        null=True,
        blank=True
    )
    addition_file_button = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    
    title_contact = models.CharField(
        _("Contact title"),
        max_length=150,
        null=True, blank=True,
    )
    contact = models.TextField(
        _("Contact"),
        blank=True
    )
    contact_image = models.ImageField(
        _("Contact image"),
        upload_to='about/',
        null=True,
        blank=True
    )
    def __str__(self):
        return self.about[:20]
    


class Social(TimeStampedModel):
    name = models.CharField(
        _("Name"),
        max_length=100
    )
    image = models.ImageField(
        _("Image"),
        upload_to='about/socials/'
    )
    url = models.URLField(        
        default='#'
    )
    rank = models.PositiveSmallIntegerField(
        default=1
    )
    
    class Meta:
        ordering = ('rank',)
        
    def __str__(self):
        return self.name
    
