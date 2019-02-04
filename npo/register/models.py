"""
"""


from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Owner(models.Model):
    """
    """
    name = models.CharField(verbose_name=_('name'), max_length=80)
    address = models.CharField(verbose_name=_('address'), max_length=80, blank=True)

    email = models.EmailField(verbose_name=_('email'), blank=True)
    phone = models.CharField(verbose_name=_('phone'), max_length=40, blank=True)

    class Meta:
        verbose_name = _('owner')
        verbose_name_plural = _('owners')

    def __str__(self):
        return self.name


class Parcel(models.Model):
    """
    """

    key = models.CharField(verbose_name=_('capakey'), max_length=20, validators=[MinLengthValidator(17), MaxLengthValidator(17)])
    owners = models.ManyToManyField(Owner, through='Ownership')

    class Meta:
        verbose_name = _('parcel')
        verbose_name_plural = _('parcels')

    def __str__(self):
        return str(self.key)


class Ownership(models.Model):
    """
    """
    parcel = models.ForeignKey(Parcel, verbose_name=_('parcel'),
        on_delete=models.PROTECT)
    owner = models.ForeignKey(Owner, verbose_name=_('owner'),
        on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('ownership')
        verbose_name_plural = _('ownerships')
