"""
"""


from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class AmphiConfig(AppConfig):
    name = 'amphi'
    verbose_name = _('Amphibian Transfer')
