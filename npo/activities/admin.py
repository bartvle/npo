"""
"""


from django.contrib.admin import ModelAdmin

from npo.admin import admin_site

from .models import Activity


class ActivityAdmin(ModelAdmin):
    list_display = ('date', 'name')
    list_display_links = ('name',)
    date_hierarchy = 'date'
    ordering = ('-date',)


admin_site.register(Activity, ActivityAdmin)
