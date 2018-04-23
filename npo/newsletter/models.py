"""
"""


from django.utils.translation import ugettext_lazy as _
from django.db import models


class Subscription(models.Model):
    """
    """

    email = models.EmailField(verbose_name=_('email'), unique=True)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('subscription')
        verbose_name_plural = _('subscriptions')
        ordering = ['email']

    def __str__(self):
        """
        """
        return self.email
