"""
"""


from npo.admin import admin_site

from .models import Subscription


admin_site.register(Subscription)
