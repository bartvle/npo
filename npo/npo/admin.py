"""
"""


from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import TruncYear


from newsletter.models import Subscription
from amphi.models import Input


def kaart(request):
    """
    """
    return render(request, 'admin/kaart.htm')


@login_required
def emails(request):
    """
    """
    emails = [s.email for s in Subscription.objects.all()]
    s = '; '.join(emails)
    return HttpResponse(s)


def overzet(request):
    """
    """
    data = Input.objects.annotate(year=TruncYear('date')).order_by().values('year').annotate(toads=Sum('toads'), frogs=Sum('frogs'), salamanders=Sum('salamanders')).order_by('-year')
    locations = Input.objects.order_by().values('location').distinct()
    data_locations = {}
    for location in locations:
        qs = Input.objects.filter(location=location['location']).annotate(year=TruncYear('date')).order_by().values('year').annotate(toads=Sum('toads'), frogs=Sum('frogs'), salamanders=Sum('salamanders')).order_by('-year')
        data_locations[Input.LOCATIONS[location['location']-1]] = qs
    return render(request, 'admin/overzet.htm', context={'data': data, 'locations': data_locations})


class AdminSite(AdminSite):
    """
    """
    site_header = 'Natuurpunt Oosterzele Admin'
    site_title = 'NPO Admin'
    index_title = 'Sitebeheer'

    def get_urls(self):
        """
        """
        urls = [
            url(r'^kaart/$', kaart),
            url(r'^emails/$', emails),
            url(r'^overzet/$', overzet),
            ]
        return super(AdminSite, self).get_urls() + urls


admin_site = AdminSite()

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
