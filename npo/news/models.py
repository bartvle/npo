"""
"""


from django.utils.translation import ugettext_lazy as _
from django.db import models


class Article(models.Model):
    """
    """

    title = models.CharField(verbose_name=_('title'), max_length=50)
    date = models.DateField(verbose_name=_('date'))
    slug = models.SlugField(verbose_name=_('slug'))
    content = models.TextField(verbose_name=_('content'))

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    def __str__(self):
        """
        """
        return self.title
