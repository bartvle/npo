"""
"""


from django.contrib.admin import ModelAdmin

from npo.admin import admin_site

from .models import Volume, Edition


class VolumeAdmin(ModelAdmin):
    list_display = ('number', 'year')
    list_display_links = ('number', 'year')


class EditionAdmin(ModelAdmin):
    list_display = ('volume', 'quarter', 'file')
    list_display_links = ('volume', 'quarter')


admin_site.register(Volume, VolumeAdmin)
admin_site.register(Edition, EditionAdmin)
