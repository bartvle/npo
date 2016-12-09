"""
"""


from django.contrib.admin import ModelAdmin

from npo.admin import admin_site

from .models import Subscription


class SubscriptionAdmin(ModelAdmin):
    list_per_page = 200

admin_site.register(Subscription, SubscriptionAdmin)
