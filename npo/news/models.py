"""
"""


from django.db import models


class Article(models.Model):
    """
    """

    title = models.CharField(max_length=50)
    date = models.DateField()
    slug = models.SlugField()
    content = models.TextField()

    class Meta:
        verbose_name = "artikel"
        verbose_name_plural = "artikels"

    def __str__(self):
        """
        """
        return self.title
