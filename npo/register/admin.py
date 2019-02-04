"""
"""


from django.contrib.admin import ModelAdmin

from npo.admin import admin_site

from .models import Parcel, Owner, Ownership


class OwnerAdmin(ModelAdmin):
    """
    """
    list_display = ('name', 'address', 'phone', 'email')
    list_display_links = ('name',)


class ParcelAdmin(ModelAdmin):
    """
    """
    list_display = ('key',)
    list_display_links = ('key',)


class OwnershipAdmin(ModelAdmin):
    """
    """
    list_display = ('parcel', 'owner')


admin_site.register(Owner, OwnerAdmin)
admin_site.register(Parcel, ParcelAdmin)
admin_site.register(Ownership, OwnershipAdmin)
