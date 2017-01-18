"""
"""


import datetime

from django.db import models


def current_year():
    """
    """
    return datetime.datetime.now().year


def current_quarter():
    """
    """
    return (datetime.datetime.now().month // 4) + 1


class Volume(models.Model):
    """
    """

    year = models.IntegerField(default=current_year)

    def __str__(self):
        """
        """
        return '%s - %s' % (self.number, self.year)

    @property
    def number(self):
        return self.year - 1993

    class Meta:
        verbose_name = "jaargang"
        verbose_name_plural = "jaargangen"
        ordering = ['-year']


class Edition(models.Model):
    """
    """

    QUARTERS = (
        (1, 'jan-feb-mrt'),
        (2, 'apr-mei-jun'),
        (3, 'jul-aug-sep'),
        (4, 'okt-nov-dec'))

    volume = models.ForeignKey(Volume, related_name='editions', on_delete=models.PROTECT)
    quarter = models.IntegerField(choices=QUARTERS, default=current_quarter)
    file = models.FileField(upload_to='magazine')

    class Meta:
        verbose_name = "editie"
        verbose_name_plural = "edities"
        ordering = ['volume', '-quarter']
