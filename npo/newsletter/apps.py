"""
"""


from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class NewsletterConfig(AppConfig):
    name = 'newsletter'
    verbose_name = _('E-newsletter')
