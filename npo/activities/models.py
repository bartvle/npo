"""
"""


from django.utils.translation import ugettext_lazy as _
from django.db import models

from djrichtextfield.models import RichTextField


class Activity(models.Model):
    """
    """

    name = models.CharField(verbose_name=_('name'), max_length=50)
    date = models.DateField(verbose_name=_('date'))
    slug = models.SlugField(verbose_name=_('slug'))
    short = models.TextField(verbose_name=_('short'), max_length=150)
    intro = RichTextField(verbose_name=_('intro'))
    practical = models.TextField(verbose_name=_('practical'))
    published = models.BooleanField(verbose_name=_('published'), default=False)

    class Meta:
        verbose_name = _('activity')
        verbose_name_plural = _('activities')
        ordering = ['date']

    def __str__(self):
        """
        """
        return self.name


class NeighboringActivity(models.Model):
    """
    """

    DIVISIONS = (
        (1, 'Boven-Schelde'),
        (2, 'Scheldeland'),
        (3, 'Houtem'),
        (4, 'Zwalmvallei'))

    name = models.CharField(verbose_name=_('name'), max_length=100)
    date = models.DateField(verbose_name=_('date'))
    text = models.TextField(verbose_name=_('text'))
    link = models.URLField(verbose_name=_('link'))
    division = models.IntegerField(verbose_name=_('division'), choices=DIVISIONS)

    class Meta:
        verbose_name = _('neighboring activity')
        verbose_name_plural = _('neighboring activities')
        ordering = ['-date']

    def __str__(self):
        """
        """
        return self.name

    def get_division_link(self):
        """
        """
        return {1: 'http://www.natuurpuntbovenschelde.be', 2: 'http://www.natuurpuntscheldeland.be', 3: 'http://www.natuurpunthoutem.be', 4: 'http://www.natuurpuntzwalmvallei.be'}[self.division]
