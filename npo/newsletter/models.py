"""
"""


from django.db import models


class Subscription(models.Model):
    """
    """

    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "inschrijving"
        verbose_name_plural = "inschrijvingen"
        ordering = ['email']

    def __str__(self):
        """
        """
        return self.email
