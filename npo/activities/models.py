"""
"""


from django.db import models


class Activity(models.Model):
    """
    """

    name = models.CharField(max_length=50)
    date = models.DateField()
    slug = models.SlugField()
    short = models.TextField(max_length=125)
    intro = models.TextField()
    practical = models.TextField()

    class Meta:
        verbose_name = "activiteit"
        verbose_name_plural = "activiteiten"

    def __str__(self):
        """
        """
        return self.name
