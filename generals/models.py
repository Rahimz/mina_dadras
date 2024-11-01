from django.db import models
from django.utils.translation import gettext_lazy as _

from tools.models import TimeStampedModel


class About(TimeStampedModel):
    about = models.TextField(
        _("About me")
    )
    image = models.ImageField(
        _("Image"),
        upload_to='about/'
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
    
