"""
"""


from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class MagazineConfig(AppConfig):
    name = 'magazine'
    verbose_name = _('Magazine')
