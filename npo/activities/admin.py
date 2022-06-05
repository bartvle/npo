"""
"""


from django.contrib.admin import ModelAdmin

from npo.admin import admin_site

from .models import Activity, NeighboringActivity


class ActivityAdmin(ModelAdmin):
    list_display = ('date', 'name')
    list_display_links = ('name',)
    date_hierarchy = 'date'
    ordering = ('-date',)


class NeighboringActivityAdmin(ModelAdmin):
    list_display = ('date', 'name')
    list_display_links = ('name',)


admin_site.register(Activity, ActivityAdmin)
admin_site.register(NeighboringActivity, NeighboringActivityAdmin)
