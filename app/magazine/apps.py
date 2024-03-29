"""
"""


from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class MagazineConfig(AppConfig):
    name = 'magazine'
    verbose_name = _('Magazine')
