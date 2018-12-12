"""
"""


from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class RegisterConfig(AppConfig):
    name = 'register'
    verbose_name = _('Register')
