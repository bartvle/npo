"""
"""


import datetime

from django.utils.translation import ugettext_lazy as _
from django.db import models


def current_year():
    """
    """
    return datetime.datetime.now().year


def current_quarter():
    """
    """
    return (datetime.datetime.now().month // 4) + 1


def upload_to(instance, filename):
    """
    """
    quarter = instance.get_quarter_display().replace('-', '')
    year = instance.volume.year
    filename = '%s%s.pdf' % (quarter, year)
    return '/'.join(['magazine', str(year), filename])


class Volume(models.Model):
    """
    """

    year = models.IntegerField(verbose_name=_('year'), default=current_year)

    def __str__(self):
        """
        """
        return '%s - %s' % (self.number, self.year)

    def _number(self):
        return self.year - 1993
    _number.short_description = _('number')
    number = property(_number)

    class Meta:
        verbose_name = _('volume')
        verbose_name_plural = _('volumes')
        ordering = ['-year']


class Edition(models.Model):
    """
    """

    QUARTERS = (
        (1, 'jan-feb-mrt'),
        (2, 'apr-mei-jun'),
        (3, 'jul-aug-sep'),
        (4, 'okt-nov-dec'))

    volume = models.ForeignKey(Volume, verbose_name=_('volume'), related_name='editions', on_delete=models.PROTECT)
    quarter = models.IntegerField(verbose_name=_('quarter'), choices=QUARTERS, default=current_quarter)
    file = models.FileField(verbose_name=_('file'), upload_to=upload_to)

    def __str__(self):
        """
        """
        return '%s - %s' % (self.volume, self.get_quarter_display())

    class Meta:
        verbose_name = _('edition')
        verbose_name_plural = _('editions')
        ordering = ['volume', '-quarter']
