"""
"""


from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse


from newsletter.models import Subscription


def kaart(request):
    """
    """
    return render(request, 'admin/kaart.htm')


def make_list(request):
    """
    """
    emails = [s.email for s in Subscription.objects.all()]
    s = '; '.join(emails)
    return HttpResponse(s)


class AdminSite(AdminSite):
    """
    """
    site_header = 'Natuurpunt Oosterzele Admin'
    site_title = 'NPO Admin'
    index_title = 'Sitebeheer'

    def get_urls(self):
        """
        """
        urls = [url(r'^kaart/$', kaart), url(r'^inschrijvingen/$', make_list)]
        return super(AdminSite, self).get_urls() + urls


admin_site = AdminSite()

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
