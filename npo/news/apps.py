"""
"""


from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'news'
    verbose_name = _('News')
