"""
"""


from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Owner(models.Model):
    """
    """
    f_name = models.CharField(verbose_name=_('f_name'), max_length=40)
    l_name = models.CharField(verbose_name=_('l_name'), max_length=40)

    name = models.CharField(verbose_name=_('name'), max_length=80, blank=True)
    address = models.CharField(verbose_name=_('address'), max_length=80, blank=True)

    street = models.CharField(verbose_name=_('street'), max_length=40,
        blank=True)
    number = models.CharField(verbose_name=_('number'), max_length=40,
        blank=True)
    municipality = models.CharField(verbose_name=_('municipality'),
        max_length=40, blank=True)

    email = models.EmailField(verbose_name=_('email'), blank=True)
    phone = models.CharField(verbose_name=_('phone'), max_length=40,
        blank=True)

    class Meta:
        verbose_name = _('owner')
        verbose_name_plural = _('owners')

    def __str__(self):
        return self.f_name + ' ' + self.l_name


class Parcel(models.Model):
    """
    """

    oidn = models.PositiveIntegerField(primary_key=True)
    key = models.CharField(verbose_name=_('key'), max_length=17, validators=[MinLengthValidator(17), MaxLengthValidator(17)], blank=True)
    owners = models.ManyToManyField(Owner, through='Ownership')

    class Meta:
        verbose_name = _('parcel')
        verbose_name_plural = _('parcels')

    def __str__(self):
        return str(self.oidn)


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
