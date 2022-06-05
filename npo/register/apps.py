"""
"""


from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class RegisterConfig(AppConfig):
    name = 'register'
    verbose_name = _('Register')
