"""
"""


from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models


class Input(models.Model):
    """
    """

    LOCATIONS = (
        (1, 'Lembergestraat'),
        (2, 'Hoek ter Hulst'),
        (3, 'Turkenhoek'),
    )

    date = models.DateField(verbose_name=_('date'))
    by = models.ForeignKey(User, verbose_name=_('by'), related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    location = models.IntegerField(verbose_name=_('location'), choices=LOCATIONS)
    toads = models.IntegerField(verbose_name=_('toads'), default=0)
    frogs = models.IntegerField(verbose_name=_('frogs'), default=0)
    salamanders = models.IntegerField(verbose_name=_('salamanders'), default=0)
    toads_death = models.IntegerField(verbose_name=_('toads death'), default=0)
    frogs_death = models.IntegerField(verbose_name=_('frogs death'), default=0)
    salamanders_death = models.IntegerField(verbose_name=_('salamanders death'), default=0)
    remark = models.TextField(verbose_name=_('remark'), blank=True, default='')

    class Meta:
        verbose_name = _('input')
        verbose_name_plural = _('inputs')
        ordering = ['-date']
