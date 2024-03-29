"""
"""


from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class ActivitiesConfig(AppConfig):
    name = 'activities'
    verbose_name = _('Activities')
