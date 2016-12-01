"""
"""


from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.conf.urls import patterns, url
from django.shortcuts import render


def kaart(request):
    """
    """
    return render(request, 'admin/kaart.htm')


class AdminSite(AdminSite):
    """
    """
    site_header = 'Natuurpunt Oosterzele Admin'

    def get_urls(self):
        """
        """
        urls = [url(r'^kaart/$', kaart)]
        return super(AdminSite, self).get_urls() + urls


admin_site = AdminSite()

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
