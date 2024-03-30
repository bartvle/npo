"""
"""


from django.contrib.admin import ModelAdmin

from frontend.admin import admin_site

from .models import Subscription


class SubscriptionAdmin(ModelAdmin):
    list_display  = ('email', 'created_at')
    list_per_page = 200
    ordering = ('-created_at',)

admin_site.register(Subscription, SubscriptionAdmin)
