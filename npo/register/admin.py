"""
"""


from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import ModelAdmin, TabularInline

from npo.admin import admin_site

from .models import Parcel, Owner, Ownership


class OwnerAdmin(ModelAdmin):
    """
    """
    list_display = ('name', 'address', 'phone', 'email')
    list_display_links = ('name',)


class OwnershipInline(TabularInline):
    """
    """
    model = Ownership
    extra = 0
    verbose_name = _('owner')
    verbose_name_plural = _('owners')


class ParcelAdmin(ModelAdmin):
    """
    """
    list_display = ('key',)
    list_display_links = ('key',)
    inlines = [OwnershipInline,]


class OwnershipAdmin(ModelAdmin):
    """
    """
    list_display = ('parcel', 'owner')



admin_site.register(Owner, OwnerAdmin)
admin_site.register(Parcel, ParcelAdmin)
admin_site.register(Ownership, OwnershipAdmin)
