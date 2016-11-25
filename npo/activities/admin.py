"""
"""


from npo.admin import admin_site

from .models import Activity


admin_site.register(Activity)
