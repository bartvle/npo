"""
"""


from django.contrib.admin import ModelAdmin

from npo.admin import admin_site

from .models import Parcel, Owner, Ownership


class ParcelAdmin(ModelAdmin):
    """
    """
    list_display = ('oidn',)


class OwnerAdmin(ModelAdmin):
    """
    """
    list_display = ('f_name', 'l_name', 'street', 'number', 'municipality',
        'phone', 'email')
    list_display_links = ('f_name', 'l_name')


class OwnershipAdmin(ModelAdmin):
    """
    """
    list_display = ('parcel', 'owner')


admin_site.register(Parcel, ParcelAdmin)
admin_site.register(Owner, OwnerAdmin)
admin_site.register(Ownership, OwnershipAdmin)
