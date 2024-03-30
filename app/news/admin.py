"""
"""


from django.contrib.admin import ModelAdmin

from frontend.admin import admin_site

from .models import Article


class ArticleAdmin(ModelAdmin):
    list_display = ('date', 'title')
    list_display_links = ('title',)


admin_site.register(Article, ArticleAdmin)
