"""
"""


from django.utils.translation import ugettext_lazy as _
from django.db import models


class Activity(models.Model):
    """
    """

    name = models.CharField(verbose_name=_('name'), max_length=50)
    date = models.DateField(verbose_name=_('date'))
    slug = models.SlugField(verbose_name=_('slug'))
    short = models.TextField(verbose_name=_('short'), max_length=125)
    intro = models.TextField(verbose_name=_('intro'))
    practical = models.TextField(verbose_name=_('practical'))

    class Meta:
        verbose_name = _('activity')
        verbose_name_plural = _('activities')
        ordering = ['-date']

    def __str__(self):
        """
        """
        return self.name
